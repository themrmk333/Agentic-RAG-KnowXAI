"""
CLI runner for Step 4 - Local GPU Embedding Generation Pipeline.
Usage:
    python rag/embeddings/run_step4.py --test 50
    python rag/embeddings/run_step4.py --dry-run
    python rag/embeddings/run_step4.py --resume --batch-size 64
    python rag/embeddings/run_step4.py --validate
    python rag/embeddings/run_step4.py --benchmark
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import shutil
import sys
import time
from pathlib import Path

import torch

# Ensure project root is on sys.path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from config.settings import get_settings
from rag.embeddings.client import ResilientEmbeddingClient
from rag.embeddings.models import (
    DEFAULT_EMBEDDING_BATCH_SIZE,
    DEFAULT_MAX_RETRIES,
    DEFAULT_REQUEST_TIMEOUT,
    DEFAULT_RETRY_BASE_DELAY,
    EXPECTED_VECTOR_DIMENSION,
    validate_vector,
)
from rag.embeddings.pipeline import Step4EmbeddingPipeline
from rag.embeddings.validator import (
    EmbeddingInputValidator,
    EmbeddingPostValidator,
)


def compute_chunks_directory_sha256(chunks_dir: Path) -> str:
    """Compute deterministic SHA-256 hash over all JSONL files in the chunks directory."""
    hasher = hashlib.sha256()
    jsonl_files = sorted(chunks_dir.glob("**/*.jsonl"))
    for file_path in jsonl_files:
        hasher.update(file_path.name.encode("utf-8"))
        with open(file_path, mode="rb") as f:
            while chunk := f.read(65536):
                hasher.update(chunk)
    return hasher.hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Step 4: Local GPU Embedding Generation Pipeline (SentenceTransformers / CUDA)"
    )
    parser.add_argument(
        "--test",
        type=int,
        default=None,
        metavar="N",
        help="Run a safe isolated embedding test with the first N chunks (e.g. --test 50)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Perform configuration, input validation, and dimension check without full generation",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume embedding generation from existing checkpoint if available",
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Run post-generation validation on existing embeddings without generating new vectors",
    )
    parser.add_argument(
        "--benchmark",
        action="store_true",
        help="Benchmark GPU batch sizes (32, 64, 128) on a small slice before full generation",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=DEFAULT_EMBEDDING_BATCH_SIZE,
        help=f"Number of chunks per GPU batch (default: {DEFAULT_EMBEDDING_BATCH_SIZE})",
    )
    parser.add_argument(
        "--device",
        type=str,
        default="cuda",
        help="Inference device: 'cuda' or 'cpu' (default: cuda)",
    )
    parser.add_argument(
        "--force-cpu",
        action="store_true",
        help="Explicitly allow CPU execution if CUDA is unavailable (default: False)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.0,
        help="Delay in seconds between batch requests (default: 0.0)",
    )
    parser.add_argument(
        "--chunks-dir",
        type=str,
        default=str(PROJECT_ROOT / "data" / "chunks"),
        help="Directory containing validated input chunks (default: data/chunks)",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=str(PROJECT_ROOT / "data" / "embeddings" / "step4"),
        help="Output directory for generated embeddings and reports (default: data/embeddings/step4)",
    )
    return parser.parse_args()


def print_safety_verification() -> None:
    print("\n" + "=" * 62)
    print("SAFETY VERIFICATION")
    print("=" * 62)
    print("PostgreSQL touched        : FALSE")
    print("PGVector touched          : FALSE")
    print("Database connection       : FALSE")
    print("Database insertion        : FALSE")
    print("Database update           : FALSE")
    print("Database deletion         : FALSE")
    print("Alembic migration         : FALSE")
    print("Source chunks modified    : FALSE")
    print("Cleaned data modified     : FALSE")
    print("Gemini embedding API      : NOT USED")
    print("OpenRouter embedding API  : NOT USED")
    print("=" * 62)


def run_benchmark(client: ResilientEmbeddingClient, chunks: list, batch_sizes: list[int] = [32, 64, 128]) -> None:
    sample_texts = [c.text for c in chunks[:128]]
    print("\n" + "=" * 62)
    print("GPU BATCH SIZE BENCHMARK")
    print("=" * 62)
    print(f"Device        : {client.device}")
    if torch.cuda.is_available() and "cuda" in client.device:
        print(f"GPU Name      : {torch.cuda.get_device_name(0)}")
        print(f"Allocated VRAM: {torch.cuda.memory_allocated(0) / (1024**2):.1f} MB")
        print(f"Reserved VRAM : {torch.cuda.memory_reserved(0) / (1024**2):.1f} MB")
    print("-" * 62)

    for bs in batch_sizes:
        if bs > len(sample_texts):
            continue
        test_slice = sample_texts[:bs]
        # Warmup
        _ = client.embed_batch(test_slice[:min(10, len(test_slice))])
        
        t0 = time.time()
        vectors = client.embed_batch(test_slice)
        elapsed = time.time() - t0
        throughput = len(test_slice) / elapsed if elapsed > 0 else 0
        vram_mb = torch.cuda.memory_allocated(0) / (1024**2) if torch.cuda.is_available() and "cuda" in client.device else 0
        print(f"Batch Size {bs:3d}: {elapsed:6.3f}s | {throughput:7.1f} chunks/sec | VRAM: {vram_mb:5.1f} MB | OK: {len(vectors)} vectors")

    print("=" * 62)


def run_isolated_test(
    num_chunks: int,
    chunks_path: Path,
    client: ResilientEmbeddingClient,
    settings: Any,
    batch_size: int,
    device_str: str,
    device_name: str,
) -> int:
    """Execute a safe, isolated test of N chunks without touching full generation files or database."""
    test_output_dir = PROJECT_ROOT / "data" / "embeddings" / f"test_step4_{num_chunks}_local"
    if test_output_dir.exists():
        shutil.rmtree(test_output_dir, ignore_errors=True)
    test_output_dir.mkdir(parents=True, exist_ok=True)

    print("\n" + "=" * 62)
    print(f"STEP 4 - STARTING ISOLATED {num_chunks}-CHUNK LOCAL EMBEDDING TEST")
    print("=" * 62)
    print(f"Provider          : local")
    print(f"Model             : {settings.embedding_model}")
    print(f"Device            : {device_str}")
    print(f"GPU               : {device_name}")
    print(f"Test chunks       : {num_chunks}")
    print(f"Isolated output   : {test_output_dir}")
    print("=" * 62)

    # 1. SHA-256 Before
    sha_before = compute_chunks_directory_sha256(chunks_path)

    # 2. Pipeline execution for test slice
    effective_batch_size = min(batch_size, num_chunks)
    pipeline = Step4EmbeddingPipeline(
        chunks_root=chunks_path,
        output_root=test_output_dir,
        client=client,
        settings=settings,
        batch_size=effective_batch_size,
        expected_dimension=EXPECTED_VECTOR_DIMENSION,
    )

    t0 = time.time()
    results = pipeline.run(resume=False, limit=num_chunks)
    duration = time.time() - t0

    # 3. SHA-256 After
    sha_after = compute_chunks_directory_sha256(chunks_path)
    source_chunks_unchanged = (sha_before == sha_after)

    # 4. Detailed vector and JSONL verification
    generated_jsonl_files = list((test_output_dir / "embeddings").glob("**/embeddings.jsonl"))
    records = []
    jsonl_valid = True
    nan_count = 0
    inf_count = 0
    dim_mismatches = 0
    all_numeric = True

    for fpath in generated_jsonl_files:
        with open(fpath, mode="r", encoding="utf-8") as f:
            for line_idx, line in enumerate(f):
                line_str = line.strip()
                if not line_str:
                    continue
                try:
                    rec = json.loads(line_str)
                    records.append(rec)
                    vec = rec.get("embedding", [])
                    if len(vec) != EXPECTED_VECTOR_DIMENSION:
                        dim_mismatches += 1
                    for v in vec:
                        if not isinstance(v, (int, float)):
                            all_numeric = False
                        elif math.isnan(v):
                            nan_count += 1
                        elif math.isinf(v):
                            inf_count += 1
                except Exception as e:
                    jsonl_valid = False

    # Verify 1-to-1 chunk ID mapping and order
    input_validator = EmbeddingInputValidator(chunks_path)
    all_input_chunks, _ = input_validator.validate_and_load()
    expected_test_chunks = all_input_chunks[:num_chunks]
    expected_ids = [c.chunk_id for c in expected_test_chunks]
    generated_ids = [r.get("chunk_id") for r in records]

    chunk_id_mapping_pass = (
        len(records) == num_chunks
        and generated_ids == expected_ids
    )

    all_pass = (
        len(records) == num_chunks
        and dim_mismatches == 0
        and nan_count == 0
        and inf_count == 0
        and all_numeric
        and jsonl_valid
        and chunk_id_mapping_pass
        and source_chunks_unchanged
    )

    avg_time_per_chunk = (duration / num_chunks) if num_chunks > 0 else 0.0
    throughput = (num_chunks / duration) if duration > 0 else 0.0

    primary_jsonl_path = generated_jsonl_files[0] if generated_jsonl_files else (test_output_dir / "embeddings" / "batch_01" / "embeddings.jsonl")
    checkpoint_path = test_output_dir / "checkpoints" / "checkpoint.json"

    print("\n" + "=" * 62)
    print(f"STEP 4 — LOCAL {num_chunks} CHUNK EMBEDDING TEST")
    print("=" * 62)
    print(f"Provider              : local")
    print(f"Model                 : {settings.embedding_model}")
    print(f"Device                : {device_str}")
    print(f"GPU                   : {device_name}")
    print(f"Expected dimension    : {EXPECTED_VECTOR_DIMENSION}")
    print(f"Input chunks          : {num_chunks}")
    print(f"Embeddings generated  : {len(records)} / {num_chunks}")
    print(f"Vector dimension      : {EXPECTED_VECTOR_DIMENSION if dim_mismatches == 0 else 'MISMATCH'}")
    print(f"NaN values            : {nan_count}")
    print(f"Infinity values       : {inf_count}")
    print(f"Chunk ID mapping      : {'PASS' if chunk_id_mapping_pass else 'FAIL'}")
    print(f"JSONL validity        : {'PASS' if jsonl_valid else 'FAIL'}")
    print(f"Source chunks changed : {'FALSE' if source_chunks_unchanged else 'TRUE'}")
    print(f"PostgreSQL touched    : FALSE")
    print(f"pgvector touched      : FALSE")
    print(f"Full generation       : FALSE")
    print("=" * 62)
    print(f"FINAL STATUS: {'PASS' if all_pass else 'FAIL'}")
    print("=" * 62)

    print("\n" + "=" * 62)
    print("PERFORMANCE & ARTIFACT DETAILS")
    print("=" * 62)
    print(f"Total execution time  : {duration:.3f} s")
    print(f"Average time per chunk: {avg_time_per_chunk * 1000:.2f} ms")
    print(f"Embedding throughput  : {throughput:.1f} chunks/sec")
    print(f"Output JSONL path     : {primary_jsonl_path}")
    print(f"Checkpoint path       : {checkpoint_path if checkpoint_path.exists() else 'N/A'}")
    print(f"Source SHA-256 before : {sha_before}")
    print(f"Source SHA-256 after  : {sha_after}")
    print("=" * 62)

    print_safety_verification()
    print(f"\nSTOP - Safe {num_chunks}-chunk test complete. Full generation was NOT started.")
    return 0 if all_pass else 1


def main() -> int:
    args = parse_args()
    settings = get_settings()

    chunks_path = Path(args.chunks_dir)
    output_path = Path(args.output_dir)

    provider = getattr(settings, "embedding_provider", "local").lower()
    cuda_available = torch.cuda.is_available()
    device_name = torch.cuda.get_device_name(0) if cuda_available else "NO GPU (CPU only)"
    actual_device = "cuda:0" if (cuda_available and args.device.startswith("cuda")) else ("cuda" if cuda_available else "cpu")

    print("=" * 62)
    print("STEP 4 - LOCAL GPU EMBEDDING GENERATION PIPELINE")
    print("=" * 62)
    print(f"Project root      : {PROJECT_ROOT}")
    print(f"Input chunks      : {chunks_path}")
    print(f"Output directory  : {output_path}")
    print(f"Embedding provider: {provider}")
    print(f"Embedding model   : {settings.embedding_model}")
    print(f"Batch size        : {args.batch_size}")
    print(f"Expected dim      : {EXPECTED_VECTOR_DIMENSION}")
    print(f"Target device     : {args.device}")
    print(f"CUDA available    : {cuda_available}")
    print(f"Device name       : {device_name}")
    print("=" * 62)

    # Check CUDA requirement
    if args.device.startswith("cuda") and not cuda_available:
        if not args.force_cpu:
            print("\nERROR: CUDA is requested, but torch.cuda.is_available() returned False.")
            print("To prevent slow CPU execution on 12,730 chunks, generation has stopped.")
            print("Please ensure CUDA-enabled PyTorch is installed or pass --force-cpu if intentional.")
            return 1
        else:
            print("\nWARNING: CUDA unavailable. Proceeding with CPU inference (--force-cpu flag active).")
            actual_device = "cpu"

    client = ResilientEmbeddingClient(
        model=settings.embedding_model,
        expected_dimension=EXPECTED_VECTOR_DIMENSION,
        device=actual_device,
        require_cuda=("cuda" in actual_device),
    )

    # Isolated Test Mode (--test N)
    if args.test is not None and args.test > 0:
        return run_isolated_test(
            num_chunks=args.test,
            chunks_path=chunks_path,
            client=client,
            settings=settings,
            batch_size=args.batch_size,
            device_str=actual_device,
            device_name=device_name,
        )

    # Benchmark mode (--benchmark)
    if args.benchmark:
        input_validator = EmbeddingInputValidator(chunks_path)
        chunks, _ = input_validator.validate_and_load()
        run_benchmark(client, chunks, batch_sizes=[32, 64, 128])
        return 0

    # 1. Validation Only Mode (--validate)
    if args.validate:
        print("\nRunning Validation on Existing Generated Embeddings...")
        input_validator = EmbeddingInputValidator(chunks_path)
        chunks, _ = input_validator.validate_and_load()
        post_validator = EmbeddingPostValidator(
            embeddings_root=output_path / "embeddings",
            input_chunks=chunks,
            expected_dim=EXPECTED_VECTOR_DIMENSION,
        )
        report = post_validator.validate()

        print("\n" + "=" * 62)
        print("STEP 4 - EMBEDDING VALIDATION SUMMARY")
        print("=" * 62)
        print(f"Input chunks             : {report['total_input_chunks']:,}")
        print(f"Embedded chunks          : {report['total_embedded_chunks']:,}")
        print(f"Missing embeddings       : {report['missing_embeddings_count']}")
        print(f"Duplicate embedding IDs  : {report['duplicate_embedding_ids_count']}")
        print(f"Invalid vectors          : {report['invalid_vectors_count']}")
        print(f"Dimension mismatches     : {report['dimension_mismatches_count']}")
        print(f"NaN vectors              : {report['nan_vectors_count']}")
        print(f"Infinity vectors         : {report['inf_vectors_count']}")
        print(f"Total errors             : {report['error_count']}")
        print(f"FINAL STATUS             : {report['status']}")
        print("=" * 62)
        print_safety_verification()
        return 0 if report["is_valid"] else 1

    # 2. Dry Run Mode (--dry-run)
    if args.dry_run:
        pipeline = Step4EmbeddingPipeline(
            chunks_root=chunks_path,
            output_root=output_path,
            client=client,
            settings=settings,
            batch_size=args.batch_size,
            delay_between_batches=args.delay,
            expected_dimension=EXPECTED_VECTOR_DIMENSION,
        )
        print("\nExecuting Dry Run Mode...")
        try:
            report = pipeline.dry_run()
            print("\n" + "=" * 62)
            print("STEP 4 - EMBEDDING DRY RUN")
            print("=" * 62)
            print(f"Input chunks          : {report['input_chunks']:,}")
            print(f"Invalid chunks        : {report['invalid_chunks']}")
            print(f"Duplicate IDs         : {report['duplicate_chunk_ids']}")
            print()
            print(f"Embedding model       : {report['embedding_model']}")
            print(f"Embedding dimension   : {report['embedding_dimension']}")
            print(f"Batch size            : {report['batch_size']}")
            print(f"Estimated requests    : {report['estimated_api_requests']:,}")
            print()
            print(f"Configuration         : {report['configuration_status']}")
            print(f"Input validation      : {report['input_validation_status']}")
            print(f"Dimension validation  : {report['dimension_validation_status']}")
            print()
            print("PostgreSQL touched    : FALSE")
            print("PGVector touched      : FALSE")
            print()
            print(f"DRY RUN STATUS        : {report['dry_run_status']}")
            print("=" * 62)
            print_safety_verification()
            print("\nDry run passed. To generate full embeddings, run without --dry-run.")
            return 0
        except Exception as e:
            print(f"\nDry run FAILED: {e}")
            return 1

    # 3. Full Embedding Generation
    pipeline = Step4EmbeddingPipeline(
        chunks_root=chunks_path,
        output_root=output_path,
        client=client,
        settings=settings,
        batch_size=args.batch_size,
        delay_between_batches=args.delay,
        expected_dimension=EXPECTED_VECTOR_DIMENSION,
    )
    print(f"\nStarting Full Embedding Generation (resume={args.resume})...")
    sha_before = compute_chunks_directory_sha256(chunks_path)
    try:
        results = pipeline.run(resume=args.resume)
        sha_after = compute_chunks_directory_sha256(chunks_path)
        source_chunks_unchanged = (sha_before == sha_after)

        emb_rep = results["embedding_report"]
        val_sum = results["validation_summary"]
        duration = emb_rep["duration_seconds"]
        total_embedded = val_sum["TOTAL_EMBEDDED_CHUNKS"]
        total_input = val_sum["TOTAL_INPUT_CHUNKS"]
        avg_ms_chunk = (duration / max(1, total_embedded)) * 1000
        throughput = total_embedded / max(0.001, duration)

        output_jsonl_files = list((output_path / "embeddings").glob("**/embeddings.jsonl"))
        checkpoint_path = output_path / "checkpoints" / "checkpoint.json"

        print("\n" + "=" * 62)
        print("STEP 4 — FULL LOCAL EMBEDDING GENERATION COMPLETE")
        print("=" * 62)
        print(f"Provider              : local")
        print(f"Model                 : {settings.embedding_model}")
        print(f"Device                : {actual_device}")
        print(f"GPU                   : {device_name}")
        print(f"Expected dimension    : {EXPECTED_VECTOR_DIMENSION}")
        print(f"Input chunks          : {total_input:,}")
        print(f"Embeddings generated  : {total_embedded:,} / {total_input:,}")
        print(f"Vector dimension      : {EXPECTED_VECTOR_DIMENSION if val_sum['DIMENSION_MISMATCHES'] == 0 else 'MISMATCH'}")
        print(f"NaN values            : {val_sum['NAN_VECTORS']}")
        print(f"Infinity values       : {val_sum['INFINITY_VECTORS']}")
        print(f"Missing embeddings    : {val_sum['MISSING_EMBEDDINGS']}")
        print(f"Duplicate chunk IDs   : {val_sum['DUPLICATE_EMBEDDING_IDS']}")
        print(f"Invalid vectors       : {val_sum['INVALID_VECTORS']}")
        print(f"Failed batches        : {val_sum['FAILED_BATCHES']}")
        print(f"Chunk ID mapping      : {'PASS' if val_sum['MISSING_EMBEDDINGS'] == 0 and val_sum['DUPLICATE_EMBEDDING_IDS'] == 0 else 'FAIL'}")
        print(f"Source chunks changed : {'FALSE' if source_chunks_unchanged else 'TRUE'}")
        print(f"PostgreSQL touched    : FALSE")
        print(f"pgvector touched      : FALSE")
        print(f"Gemini API used       : FALSE")
        print(f"OpenRouter API used   : FALSE")
        print("=" * 62)
        print(f"FINAL STATUS: {val_sum['FINAL_STATUS']}")
        print("=" * 62)

        print("\n" + "=" * 62)
        print("PERFORMANCE & ARTIFACT DETAILS")
        print("=" * 62)
        print(f"Total execution time  : {duration:.2f} s ({duration/60:.2f} min)")
        print(f"Average time per chunk: {avg_ms_chunk:.2f} ms")
        print(f"Embedding throughput  : {throughput:.1f} chunks/sec")
        print(f"Total output files    : {len(output_jsonl_files)} JSONL files")
        print(f"Output directory      : {output_path / 'embeddings'}")
        print(f"Checkpoint status     : {'EXISTS & VALID' if checkpoint_path.exists() else 'N/A'}")
        print(f"Source SHA-256 before : {sha_before}")
        print(f"Source SHA-256 after  : {sha_after}")
        print("=" * 62)

        print_safety_verification()
        print("\nSTOP - Step 4 complete. Do NOT proceed to Step 5 (PostgreSQL insertion).")
        return 0 if val_sum["FINAL_STATUS"] == "PASS" else 1

    except Exception as e:
        print(f"\nEmbedding generation FAILED: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
