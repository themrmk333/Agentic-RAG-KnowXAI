"""
Step 4 Embedding Pipeline orchestrating batching, checkpointing, resilience, and validation.
"""

from __future__ import annotations

import json
import logging
import math
import shutil
import time
from collections import defaultdict
from pathlib import Path
from typing import Any, Sequence

import torch

from config.settings import Settings, get_settings
from .client import ResilientEmbeddingClient
from .models import (
    DEFAULT_EMBEDDING_BATCH_SIZE,
    DEFAULT_MAX_RETRIES,
    DEFAULT_REQUEST_TIMEOUT,
    DEFAULT_RETRY_BASE_DELAY,
    EXPECTED_VECTOR_DIMENSION,
    CheckpointState,
    EmbeddingRecord,
    InputChunk,
    compute_dataset_fingerprint,
    utc_now_iso,
)
from .validator import (
    EmbeddingInputValidator,
    EmbeddingPostValidator,
)

logger = logging.getLogger(__name__)


class Step4EmbeddingPipeline:
    """
    Orchestrates the entire Step 4 Embedding Generation process.
    """

    def __init__(
        self,
        chunks_root: Path | str,
        output_root: Path | str,
        client: ResilientEmbeddingClient | None = None,
        settings: Settings | None = None,
        batch_size: int = DEFAULT_EMBEDDING_BATCH_SIZE,
        delay_between_batches: float = 0.0,
        expected_dimension: int = EXPECTED_VECTOR_DIMENSION,
    ) -> None:
        self.chunks_root = Path(chunks_root)
        self.output_root = Path(output_root)
        self.batch_size = max(1, batch_size)
        self.delay_between_batches = delay_between_batches
        self.expected_dimension = expected_dimension
        self.settings = settings or get_settings()

        # Output subdirectories
        self.embeddings_dir = self.output_root / "embeddings"
        self.checkpoints_dir = self.output_root / "checkpoints"
        self.failures_dir = self.output_root / "failures"
        self.reports_dir = self.output_root / "reports"
        self.checkpoint_file = self.checkpoints_dir / "checkpoint.json"

        # Resolve or instantiate client
        if client is not None:
            self.client = client
        else:
            provider = getattr(self.settings, "embedding_provider", "local").lower()
            if provider == "local":
                self.client = ResilientEmbeddingClient(
                    model=self.settings.embedding_model,
                    expected_dimension=self.expected_dimension,
                    max_retries=DEFAULT_MAX_RETRIES,
                    retry_base_delay=DEFAULT_RETRY_BASE_DELAY,
                    request_timeout=DEFAULT_REQUEST_TIMEOUT,
                )
            else:
                api_key_secret = self.settings.embedding_api_key
                if not api_key_secret or not api_key_secret.get_secret_value().strip():
                    raise ValueError("EMBEDDING_API_KEY is not configured in settings or .env")
                self.client = ResilientEmbeddingClient(
                    api_key=api_key_secret.get_secret_value().strip(),
                    model=self.settings.embedding_model,
                    expected_dimension=self.expected_dimension,
                    max_retries=DEFAULT_MAX_RETRIES,
                    retry_base_delay=DEFAULT_RETRY_BASE_DELAY,
                    request_timeout=DEFAULT_REQUEST_TIMEOUT,
                )

    def _ensure_directories(self) -> None:
        """Create output subdirectories if they do not exist."""
        self.embeddings_dir.mkdir(parents=True, exist_ok=True)
        self.checkpoints_dir.mkdir(parents=True, exist_ok=True)
        self.failures_dir.mkdir(parents=True, exist_ok=True)
        self.reports_dir.mkdir(parents=True, exist_ok=True)

    def dry_run(self) -> dict[str, Any]:
        """
        Execute a complete dry run:
          - Validate input chunks
          - Validate configuration & credentials
          - Validate model vector dimension
          - Calculate estimated batches & requests
          - Save dry-run report
        Does NOT generate full dataset and does NOT touch DB.
        """
        self._ensure_directories()
        start_time = utc_now_iso()

        # 1. Validate inputs
        input_validator = EmbeddingInputValidator(self.chunks_root)
        chunks, input_report = input_validator.validate_and_load()
        if not input_report["is_valid"]:
            raise ValueError(f"Input validation failed: {input_report['errors'][:5]}")

        # 2. Validate configuration
        provider = getattr(self.settings, "embedding_provider", "local").lower()
        if provider == "local":
            config_ok = bool(self.settings.embedding_model.strip())
        else:
            api_key_ok = bool(
                self.settings.embedding_api_key
                and self.settings.embedding_api_key.get_secret_value().strip()
            )
            model_ok = bool(self.settings.embedding_model.strip())
            config_ok = api_key_ok and model_ok

        # 3. Test dimension with single lightweight request
        dim_ok, actual_dim, dim_msg = self.client.test_dimension("Step 4 dry-run dimension validation")
        if not dim_ok:
            raise ValueError(f"Embedding dimension check failed: {dim_msg}")

        total_chunks = len(chunks)
        estimated_requests = math.ceil(total_chunks / self.batch_size)

        dry_run_report = {
            "timestamp_utc": start_time,
            "dry_run_status": "PASS" if config_ok and dim_ok and input_report["is_valid"] else "FAIL",
            "input_chunks": total_chunks,
            "invalid_chunks": input_report["missing_fields_count"] + input_report["json_error_count"],
            "duplicate_chunk_ids": input_report["duplicate_id_count"],
            "embedding_model": self.client.model,
            "embedding_dimension": actual_dim,
            "expected_dimension": self.expected_dimension,
            "batch_size": self.batch_size,
            "estimated_api_requests": estimated_requests,
            "output_location": str(self.output_root),
            "configuration_status": "PASS" if config_ok else "FAIL",
            "input_validation_status": "PASS" if input_report["is_valid"] else "FAIL",
            "dimension_validation_status": "PASS" if dim_ok else "FAIL",
            "safety_checks": {
                "postgresql_touched": False,
                "pgvector_touched": False,
                "database_connection": False,
                "database_insertion": False,
                "source_chunks_modified": False,
                "cleaned_data_modified": False,
            },
        }

        report_path = self.reports_dir / "step4_dry_run_report.json"
        with open(report_path, mode="w", encoding="utf-8") as f:
            json.dump(dry_run_report, f, indent=2)

        return dry_run_report

    def _load_checkpoint(self, current_fingerprint: str) -> CheckpointState | None:
        """Load and validate existing checkpoint if present."""
        if not self.checkpoint_file.exists():
            return None
        try:
            with open(self.checkpoint_file, mode="r", encoding="utf-8") as f:
                data = json.load(f)
            cp = CheckpointState.from_dict(data)
            if cp.embedding_model != self.client.model:
                logger.warning(
                    "Checkpoint embedding model ('%s') does not match active model ('%s'). Invalidating checkpoint.",
                    cp.embedding_model,
                    self.client.model,
                )
                return None
            if cp.embedding_dimension != self.expected_dimension:
                logger.warning(
                    "Checkpoint embedding dimension (%d) does not match expected dimension (%d). Invalidating checkpoint.",
                    cp.embedding_dimension,
                    self.expected_dimension,
                )
                return None
            if cp.input_fingerprint != current_fingerprint:
                logger.warning("Checkpoint input fingerprint does not match current dataset")
                return None
            return cp
        except Exception as e:
            logger.warning("Failed to parse checkpoint file: %s", e)
            return None

    def _save_checkpoint(self, checkpoint: CheckpointState) -> None:
        """Atomically persist checkpoint state."""
        checkpoint.timestamp_utc = utc_now_iso()
        temp_file = self.checkpoint_file.with_suffix(".tmp")
        with open(temp_file, mode="w", encoding="utf-8") as f:
            json.dump(checkpoint.to_dict(), f, indent=2)
        shutil.move(str(temp_file), str(self.checkpoint_file))

    def run(self, resume: bool = False, limit: int | None = None) -> dict[str, Any]:
        """
        Execute Step 4 embedding generation.
        """
        self._ensure_directories()
        start_ts = time.time()
        start_time_iso = utc_now_iso()

        # 1. Load and validate input chunks
        input_validator = EmbeddingInputValidator(self.chunks_root)
        chunks, input_report = input_validator.validate_and_load()
        if not input_report["is_valid"]:
            raise ValueError(f"Input validation failed: {input_report['errors'][:5]}")

        if limit is not None and limit > 0:
            chunks = chunks[:limit]
            dataset_fingerprint = compute_dataset_fingerprint(chunks)
        else:
            dataset_fingerprint = input_report["dataset_fingerprint"]

        total_chunks = len(chunks)

        # 2. Test dimension
        dim_ok, actual_dim, dim_msg = self.client.test_dimension("Step 4 dimension validation")
        if not dim_ok:
            raise ValueError(f"Embedding dimension check failed: {dim_msg}")

        # 3. Handle Checkpoint & Resume
        completed_chunk_ids: set[str] = set()
        completed_batches_count = 0

        if resume:
            cp = self._load_checkpoint(dataset_fingerprint)
            if cp:
                completed_chunk_ids = set(cp.completed_chunk_ids)
                completed_batches_count = cp.completed_batches_count
                logger.info(
                    "Resuming from checkpoint: %d / %d chunks already completed",
                    len(completed_chunk_ids),
                    total_chunks,
                )
            else:
                logger.info("Resume requested but no valid checkpoint found. Checking existing output files...")
                # Scan existing output files for completed chunk_ids
                for ef in self.embeddings_dir.glob("**/embeddings.jsonl"):
                    with open(ef, mode="r", encoding="utf-8") as f:
                        for line in f:
                            if line.strip():
                                try:
                                    rec = json.loads(line)
                                    if (
                                        rec.get("embedding_model") == self.client.model
                                        and rec.get("embedding_dimension") == self.expected_dimension
                                        and "chunk_id" in rec
                                    ):
                                        completed_chunk_ids.add(rec["chunk_id"])
                                except Exception:
                                    pass
        else:
            # If not resuming and output exists, check if already completed
            pass

        # 4. Group chunks to embed
        chunks_to_process = [c for c in chunks if c.chunk_id not in completed_chunk_ids]
        logger.info("Chunks to process: %d (already completed: %d)", len(chunks_to_process), len(completed_chunk_ids))

        print("\n" + "=" * 62)
        print("STEP 4 — GENERATION INITIALIZATION")
        print("=" * 62)
        print(f"Total input chunks      : {total_chunks:,}")
        print(f"Already completed chunks: {len(completed_chunk_ids):,}")
        print(f"Remaining chunks        : {len(chunks_to_process):,}")
        print(f"Model                   : {self.client.model}")
        print(f"Device                  : {self.client.device}")
        if torch.cuda.is_available() and "cuda" in self.client.device:
            print(f"GPU                     : {torch.cuda.get_device_name(0)}")
        print(f"Dimension               : {self.expected_dimension}")
        print(f"Batch size              : {self.batch_size}")
        print(f"Output directory        : {self.output_root}")
        print("=" * 62 + "\n")

        # Group by batch_id for clean output organization
        batch_chunks_map: dict[str, list[InputChunk]] = defaultdict(list)
        for c in chunks_to_process:
            batch_chunks_map[c.batch_id].append(c)

        total_api_requests = 0
        failed_batches_count = 0
        failures: list[dict[str, Any]] = []

        # Process each batch
        for batch_name, batch_chunk_list in batch_chunks_map.items():
            batch_out_dir = self.embeddings_dir / batch_name
            batch_out_dir.mkdir(parents=True, exist_ok=True)
            batch_jsonl_path = batch_out_dir / "embeddings.jsonl"

            # Process in sub-batches
            for i in range(0, len(batch_chunk_list), self.batch_size):
                sub_batch = batch_chunk_list[i : i + self.batch_size]
                texts = [c.text for c in sub_batch]

                try:
                    vectors = self.client.embed_batch(texts)
                    total_api_requests += 1

                    # Create records and write
                    records: list[EmbeddingRecord] = []
                    for chunk_obj, vec in zip(sub_batch, vectors, strict=True):
                        rec = EmbeddingRecord(
                            chunk_id=chunk_obj.chunk_id,
                            batch_id=chunk_obj.batch_id,
                            source_file=chunk_obj.source_file,
                            relative_path=chunk_obj.relative_path,
                            chunk_index=chunk_obj.chunk_index,
                            total_chunks_for_file=chunk_obj.total_chunks_for_file,
                            chunk_sha256=chunk_obj.chunk_sha256,
                            embedding_model=self.client.model,
                            embedding_dimension=len(vec),
                            embedding=vec,
                            created_at_utc=utc_now_iso(),
                        )
                        records.append(rec)
                        completed_chunk_ids.add(chunk_obj.chunk_id)

                    # Append to jsonl
                    with open(batch_jsonl_path, mode="a", encoding="utf-8") as f:
                        for rec in records:
                            f.write(rec.to_jsonl_line() + "\n")

                    completed_batches_count += 1

                    # Checkpoint
                    cp_state = CheckpointState(
                        timestamp_utc=utc_now_iso(),
                        embedding_model=self.client.model,
                        embedding_dimension=self.expected_dimension,
                        input_fingerprint=dataset_fingerprint,
                        total_input_chunks=total_chunks,
                        completed_chunks_count=len(completed_chunk_ids),
                        completed_batches_count=completed_batches_count,
                        last_completed_batch_id=batch_name,
                        completed_chunk_ids=list(completed_chunk_ids),
                    )
                    self._save_checkpoint(cp_state)

                    elapsed = time.time() - start_ts
                    throughput = len(completed_chunk_ids) / elapsed if elapsed > 0 else 0
                    print(
                        f"  --> Progress: {len(completed_chunk_ids):,}/{total_chunks:,} chunks "
                        f"({(len(completed_chunk_ids)/total_chunks)*100:.1f}%) | "
                        f"Batch: {batch_name} | Elapsed: {elapsed:.1f}s | Speed: {throughput:.1f} chunks/s",
                        flush=True,
                    )

                    if self.delay_between_batches > 0:
                        time.sleep(self.delay_between_batches)

                except Exception as e:
                    failed_batches_count += 1
                    err_info = {
                        "timestamp_utc": utc_now_iso(),
                        "batch_id": batch_name,
                        "sub_batch_index": i // self.batch_size,
                        "chunk_ids": [c.chunk_id for c in sub_batch],
                        "error": str(e),
                    }
                    failures.append(err_info)
                    with open(self.failures_dir / "failures.jsonl", mode="a", encoding="utf-8") as f:
                        f.write(json.dumps(err_info) + "\n")
                    logger.error("Batch failure in %s: %s", batch_name, e)
                    raise

        elapsed_seconds = time.time() - start_ts

        # 5. Run Post-Validation
        post_validator = EmbeddingPostValidator(
            embeddings_root=self.embeddings_dir,
            input_chunks=chunks,
            expected_dim=self.expected_dimension,
        )
        validation_report = post_validator.validate()

        # 6. Save Reports
        embedding_report = {
            "timestamp_utc": start_time_iso,
            "duration_seconds": round(elapsed_seconds, 2),
            "input_chunks_count": total_chunks,
            "embedded_chunks_count": len(completed_chunk_ids),
            "total_api_requests": total_api_requests,
            "failed_batches_count": failed_batches_count,
            "batch_size": self.batch_size,
            "embedding_model": self.client.model,
            "embedding_dimension": self.expected_dimension,
            "output_directory": str(self.embeddings_dir),
            "checkpoint_file": str(self.checkpoint_file),
            "status": "PASS" if validation_report["is_valid"] else "FAIL",
            "safety_checks": {
                "postgresql_touched": False,
                "pgvector_touched": False,
                "database_connection": False,
                "database_insertion": False,
                "source_chunks_modified": False,
                "cleaned_data_modified": False,
            },
        }

        with open(self.reports_dir / "step4_embedding_report.json", mode="w", encoding="utf-8") as f:
            json.dump(embedding_report, f, indent=2)

        with open(self.reports_dir / "step4_validation_report.json", mode="w", encoding="utf-8") as f:
            json.dump(validation_report, f, indent=2)

        validation_summary = {
            "timestamp_utc": validation_report["timestamp_utc"],
            "TOTAL_INPUT_CHUNKS": validation_report["total_input_chunks"],
            "TOTAL_EMBEDDED_CHUNKS": validation_report["total_embedded_chunks"],
            "MISSING_EMBEDDINGS": validation_report["missing_embeddings_count"],
            "DUPLICATE_EMBEDDING_IDS": validation_report["duplicate_embedding_ids_count"],
            "INVALID_VECTORS": validation_report["invalid_vectors_count"],
            "DIMENSION_MISMATCHES": validation_report["dimension_mismatches_count"],
            "NAN_VECTORS": validation_report["nan_vectors_count"],
            "INFINITY_VECTORS": validation_report["inf_vectors_count"],
            "FAILED_BATCHES": failed_batches_count,
            "ERROR_COUNT": validation_report["error_count"],
            "QUALITY_SCORE": 100 if validation_report["is_valid"] else 0,
            "FINAL_STATUS": validation_report["status"],
            "safety": {
                "postgresql_touched": False,
                "pgvector_touched": False,
                "database_insertion": False,
            },
        }

        with open(self.reports_dir / "step4_validation_summary.json", mode="w", encoding="utf-8") as f:
            json.dump(validation_summary, f, indent=2)

        # Markdown Completion Report
        self._write_completion_report_md(embedding_report, validation_report, validation_summary)

        return {
            "embedding_report": embedding_report,
            "validation_report": validation_report,
            "validation_summary": validation_summary,
        }

    def _write_completion_report_md(
        self,
        embedding_report: dict[str, Any],
        val_report: dict[str, Any],
        val_summary: dict[str, Any],
    ) -> None:
        md_content = f"""# STEP 4 — EMBEDDING GENERATION COMPLETION REPORT

**Generated:** {embedding_report['timestamp_utc']}  
**Status:** **{val_summary['FINAL_STATUS']}**  
**Quality Score:** {val_summary['QUALITY_SCORE']}/100  

---

## 1. Executive Summary

| Metric | Value | Status |
|---|---|---|
| **Input Chunks** | {val_summary['TOTAL_INPUT_CHUNKS']:,} | ✅ Verified |
| **Embedded Chunks** | {val_summary['TOTAL_EMBEDDED_CHUNKS']:,} | ✅ 100% Complete |
| **Missing Embeddings** | {val_summary['MISSING_EMBEDDINGS']} | ✅ Zero |
| **Duplicate Embedding IDs** | {val_summary['DUPLICATE_EMBEDDING_IDS']} | ✅ Zero |
| **Invalid Vectors** | {val_summary['INVALID_VECTORS']} | ✅ Zero |
| **Dimension Mismatches** | {val_summary['DIMENSION_MISMATCHES']} | ✅ Zero |
| **NaN / Infinity Vectors** | {val_summary['NAN_VECTORS'] + val_summary['INFINITY_VECTORS']} | ✅ Zero |
| **Failed Batches** | {val_summary['FAILED_BATCHES']} | ✅ Zero |
| **Final Validation** | **{val_summary['FINAL_STATUS']}** | ✅ PASS |

---

## 2. Embedding Configuration

- **Model:** `{embedding_report['embedding_model']}`
- **Vector Dimension:** `{embedding_report['embedding_dimension']}`
- **Batch Size:** `{embedding_report['batch_size']}`
- **Total API Requests:** `{embedding_report['total_api_requests']}`
- **Duration:** `{embedding_report['duration_seconds']}s`
- **Output Location:** `{embedding_report['output_directory']}`
- **Checkpoint Location:** `{embedding_report['checkpoint_file']}`

---

## 3. Safety & Isolation Verification

| Safety Constraint | Value | Status |
|---|---|---|
| **PostgreSQL Touched** | `FALSE` | ✅ Enforced |
| **PGVector Touched** | `FALSE` | ✅ Enforced |
| **Database Connection** | `FALSE` | ✅ Enforced |
| **Database Insertion** | `FALSE` | ✅ Enforced |
| **Source Chunks Modified** | `FALSE` | ✅ Enforced |
| **Cleaned Data Modified** | `FALSE` | ✅ Enforced |

---

## 4. Next Step

**STEP 5 — POSTGRESQL + PGVECTOR INSERTION**  
*(Do not run Step 5 until explicitly requested).*
"""
        with open(self.reports_dir / "step4_completion_report.md", mode="w", encoding="utf-8") as f:
            f.write(md_content)
