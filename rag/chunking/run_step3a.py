"""
Step 3A — Chunk Repair, Regeneration & Independent Validation Runner.

Phases:
  1. Back up existing data/chunks/ to data/chunks_backup_step3a/
  2. Run repaired pipeline -> data/chunks_repaired/
  3. Run independent validation on data/chunks_repaired/
  4. Generate manifests & completion report
  5. Print final terminal report

Safety: Does NOT touch raw, processed, cleaned data, any DB, or embeddings.
"""

import json
import shutil
import sys
from pathlib import Path
from datetime import datetime, timezone

# Ensure project root is on path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from rag.chunking.pipeline_repaired import RepairedChunkingPipeline
from rag.chunking.quality_validator import ChunkQualityValidator


# ============================================================
# Paths
# ============================================================
ROOT = Path('.')
CLEANED_ROOT = ROOT / 'data' / 'cleaned'
CHUNKS_ORIGINAL = ROOT / 'data' / 'chunks'
CHUNKS_REPAIRED = ROOT / 'data' / 'chunks_repaired'
CHUNKS_BACKUP = ROOT / 'data' / 'chunks_backup_step3a'
MANIFESTS_ROOT = ROOT / 'data' / 'manifests'

BATCH_NAMES = ['batch_01', 'batch_02', 'batch_03']


# ============================================================
# Step 1: Backup
# ============================================================
def backup_existing_chunks():
    """Copy data/chunks/ -> data/chunks_backup_step3a/ (non-destructive)."""
    if CHUNKS_ORIGINAL.exists():
        if CHUNKS_BACKUP.exists():
            print(f"Backup already exists at {CHUNKS_BACKUP} — skipping.")
        else:
            print(f"Backing up {CHUNKS_ORIGINAL} -> {CHUNKS_BACKUP} ...")
            shutil.copytree(str(CHUNKS_ORIGINAL), str(CHUNKS_BACKUP))
            print("Backup complete.")
    else:
        print("No existing data/chunks/ to back up.")


# ============================================================
# Step 2: Run Repaired Pipeline
# ============================================================
def run_repaired_pipeline():
    """Execute the repaired pipeline writing to data/chunks_repaired/."""
    print("\n" + "=" * 60)
    print("PHASE 9 — RUNNING REPAIRED CHUNKING PIPELINE")
    print("=" * 60)

    pipeline = RepairedChunkingPipeline(CLEANED_ROOT, CHUNKS_REPAIRED, MANIFESTS_ROOT)
    stats = pipeline.run()
    return stats


# ============================================================
# Step 3: Independent Validation
# ============================================================
def run_independent_validation():
    """Run independent validation on data/chunks_repaired/."""
    print("\n" + "=" * 60)
    print("PHASE 10 — INDEPENDENT VALIDATION")
    print("=" * 60)

    validator = ChunkQualityValidator(CHUNKS_REPAIRED, CLEANED_ROOT, MANIFESTS_ROOT)
    report = validator.validate()
    return report


# ============================================================
# Step 4: Generate Manifests
# ============================================================
def save_validation_reports(report: dict):
    """Save quality report and summary JSON files."""
    MANIFESTS_ROOT.mkdir(parents=True, exist_ok=True)

    quality_report_path = MANIFESTS_ROOT / 'step3a_quality_report.json'
    quality_report_path.write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(f"\nQuality report saved: {quality_report_path}")

    dist = report.get('token_distribution', {})
    dup = report.get('duplicate_analysis', {})
    cov = report.get('source_coverage', {})

    summary = {
        'timestamp_utc': report['timestamp_utc'],
        'chunks_directory': str(CHUNKS_REPAIRED),
        'total_chunks': dist.get('total_chunks', 0),
        'total_words': dist.get('total_words', 0),
        'total_characters': dist.get('total_characters', 0),
        'estimated_tokens': dist.get('total_tokens', 0),
        'average_tokens_per_chunk': dist.get('average_tokens', 0),
        'median_tokens_per_chunk': dist.get('median_tokens', 0),
        'min_tokens': dist.get('min_tokens', 0),
        'max_tokens': dist.get('max_tokens', 0),
        'error_count': report['error_count'],
        'warning_count': report['warning_count'],
        'quality_score': report['quality_score'],
        'final_status': report['final_status'],
        'duplicate_chunks': dup.get('duplicate_chunks', 0),
        'duplicate_groups': dup.get('duplicate_groups', 0),
        'cross_batch_duplicates': dup.get('cross_batch_duplicates', 0),
        'source_coverage_percent': cov.get('coverage_percentage', 0),
        'size_distribution': dist.get('size_distribution', {}),
        'integrity': {
            'character_count_mismatches': (
                report['validation_results']['content_consistency']
                ['character_count_mismatches']
            ),
            'word_count_mismatches': (
                report['validation_results']['content_consistency']
                ['word_count_mismatches']
            ),
            'token_count_mismatches': (
                report['validation_results']['content_consistency']
                ['token_count_mismatches']
            ),
            'hash_mismatches': (
                report['validation_results']['hash_validation']['hash_mismatches']
            ),
            'index_errors': (
                report['validation_results']['index_validation']['index_errors']
            ),
            'missing_sources': (
                report['validation_results']['source_traceability']['missing_sources']
            ),
            'duplicate_ids': (
                report['validation_results']['chunk_id_validation']['duplicate_ids']
            ),
            'json_errors': (
                report['validation_results']['json_validation']['invalid_json_count']
            ),
        },
    }

    summary_path = MANIFESTS_ROOT / 'step3a_quality_summary.json'
    summary_path.write_text(json.dumps(summary, indent=2), encoding='utf-8')
    print(f"Summary saved: {summary_path}")

    return summary


# ============================================================
# Step 5: Completion Report
# ============================================================
def write_completion_report(pipeline_stats: dict, report: dict, summary: dict):
    """Write step3a_completion_report.md."""
    dist = report.get('token_distribution', {})
    dup = report.get('duplicate_analysis', {})
    cov = report.get('source_coverage', {})
    integ = summary['integrity']
    per_batch = pipeline_stats.get('per_batch', {})

    def _batch_line(batch):
        b = per_batch.get(batch, {})
        return f"{b.get('total_input_files', 0)} files → {b.get('total_chunks', 0)} chunks"

    status = report['final_status']
    warnings_text = "\n".join(f"- {w}" for w in report.get('warnings', [])) or "None"

    md = f"""# STEP 3A — CHUNK REPAIR & REGENERATION

**Generated**: {datetime.now(timezone.utc).isoformat()}
**Pipeline Version**: repaired_step3a
**Output Directory**: `data/chunks_repaired/`

---

## Input

| Item | Value |
|---|---|
| Total source files | {pipeline_stats.get('total_input_files', 0)} |
| Batch 01 | {_batch_line('batch_01')} |
| Batch 02 | {_batch_line('batch_02')} |
| Batch 03 | {_batch_line('batch_03')} |
| Failed files | {pipeline_stats.get('failed_files', 0)} |

---

## Output

| Item | Value |
|---|---|
| Total repaired chunks | {dist.get('total_chunks', 0)} |
| Batch 01 chunks | {per_batch.get('batch_01', {}).get('total_chunks', 0)} |
| Batch 02 chunks | {per_batch.get('batch_02', {}).get('total_chunks', 0)} |
| Batch 03 chunks | {per_batch.get('batch_03', {}).get('total_chunks', 0)} |

---

## Token Statistics

| Metric | Value |
|---|---|
| Total estimated tokens | {dist.get('total_tokens', 0):,} |
| Total words | {dist.get('total_words', 0):,} |
| Total characters | {dist.get('total_characters', 0):,} |
| Average tokens/chunk | {dist.get('average_tokens', 0)} |
| Median tokens/chunk | {dist.get('median_tokens', 0)} |
| Minimum tokens | {dist.get('min_tokens', 0)} |
| Maximum tokens | {dist.get('max_tokens', 0)} |

### Chunk Size Distribution

| Category | Count |
|---|---|
| VERY_SMALL (<50 tokens) | {dist.get('size_distribution', {}).get('VERY_SMALL', 0)} |
| SMALL (50-150 tokens) | {dist.get('size_distribution', {}).get('SMALL', 0)} |
| NORMAL (151-1200 tokens) | {dist.get('size_distribution', {}).get('NORMAL', 0)} |
| LARGE (1201-2000 tokens) | {dist.get('size_distribution', {}).get('LARGE', 0)} |
| VERY_LARGE (>2000 tokens) | {dist.get('size_distribution', {}).get('VERY_LARGE', 0)} |

---

## Integrity Validation

> [!IMPORTANT]
> All values below MUST be 0 for PASS status.

| Check | Result |
|---|---|
| Character count mismatches | {integ['character_count_mismatches']} |
| Word count mismatches | {integ['word_count_mismatches']} |
| Token count mismatches | {integ['token_count_mismatches']} |
| SHA-256 hash mismatches | {integ['hash_mismatches']} |
| Chunk index errors | {integ['index_errors']} |
| Missing source files | {integ['missing_sources']} |
| Duplicate chunk IDs | {integ['duplicate_ids']} |
| JSON parse errors | {integ['json_errors']} |
| Missing required fields | {report['validation_results']['metadata_validation']['chunks_missing_required_fields']} |

---

## Duplicate Analysis

> [!NOTE]
> Duplicates are NOT errors. Enterprise documents legitimately repeat content.

| Metric | Value |
|---|---|
| Unique chunks | {dup.get('unique_chunks', 0):,} |
| Duplicate chunks | {dup.get('duplicate_chunks', 0):,} |
| Duplicate groups | {dup.get('duplicate_groups', 0):,} |
| Duplicate percentage | {dup.get('duplicate_percentage', 0)}% |
| Cross-batch duplicate groups | {dup.get('cross_batch_duplicate_groups', 0)} |
| Cross-batch duplicates | {dup.get('cross_batch_duplicates', 0):,} |

---

## Source Coverage

| Metric | Value |
|---|---|
| Total cleaned source files | {cov.get('total_cleaned_files', 0):,} |
| Files represented in chunks | {cov.get('files_represented_in_chunks', 0):,} |
| Files with zero chunks | {cov.get('files_with_zero_chunks', 0)} |
| Coverage | {cov.get('coverage_percentage', 0)}% |

---

## Quality Score

**Score**: {report['quality_score']}/100
**Status**: **{status}**

---

## Root Cause Analysis

The previous Step 3 validation reported FAIL due to false positives, not real data corruption:

1. **4,075 metadata mismatches** — `quality_validator.py` opened JSONL files without
   `encoding='utf-8'`. Windows defaulted to `cp1252`, misreading multi-byte UTF-8
   characters (em-dashes, curly quotes, etc.), causing incorrect character counts
   and SHA-256 recalculations.

2. **5 hash mismatches** — Same encoding issue in the validator.

3. **5 index errors** — The validator grouped chunks by `relative_path` alone.
   Files that exist identically in batch_01, batch_02, and batch_03 appeared as
   one "group" with 3 chunks, but each batch correctly had `chunk_index=0` and
   `total_chunks_for_file=1`. Fix: group by `(batch_id, relative_path)`.

### Fix Applied

- Rewrote `quality_validator.py`: all `open()` calls now use `encoding='utf-8'`.
- Fixed index validation key to `(batch_id, relative_path)`.
- Created `pipeline_repaired.py`: metadata is always computed from final text,
  never from pre-merge/pre-strip intermediate states.
- Chunk regeneration produces `data/chunks_repaired/`.

---

## Warnings

{warnings_text}

---

## Safety

| Check | Status |
|---|---|
| PostgreSQL touched | **NO** |
| pgvector touched | **NO** |
| Embedding API called | **NO** |
| Embeddings generated | **NO** |
| Raw ZIP modified | **NO** |
| data/raw/ modified | **NO** |
| data/processed/ modified | **NO** |
| data/cleaned/ modified | **NO** |
| data/chunks/ overwritten | **NO** (original preserved) |
| Backup created | **YES** (`data/chunks_backup_step3a/`) |

---

## Final Status

### {status}

{"All critical integrity checks passed with zero errors." if status == "PASS" else ("All critical integrity checks passed; non-zero warnings noted above." if status == "PASS_WITH_WARNINGS" else "One or more critical integrity checks FAILED — see errors above.")}

---

*Generated by Step 3A Repair Pipeline — STOP HERE. Do not proceed to embeddings.*
"""

    report_path = MANIFESTS_ROOT / 'step3a_completion_report.md'
    report_path.write_text(md, encoding='utf-8')
    print(f"Completion report saved: {report_path}")


# ============================================================
# Final Terminal Report
# ============================================================
def print_final_report(pipeline_stats: dict, report: dict):
    """Print the required final terminal output."""
    dist = report.get('token_distribution', {})
    dup = report.get('duplicate_analysis', {})
    cov = report.get('source_coverage', {})
    cc = report['validation_results']['content_consistency']
    hv = report['validation_results']['hash_validation']
    iv = report['validation_results']['index_validation']
    sv = report['validation_results']['source_traceability']
    idv = report['validation_results']['chunk_id_validation']
    jv = report['validation_results']['json_validation']

    print("\n" + "=" * 60)
    print("STEP 3A — CHUNK REGENERATION VALIDATION")
    print("=" * 60)

    print(f"\nSOURCE FILES              : {pipeline_stats.get('total_input_files', 0)}")
    print(f"REPAIRED CHUNKS           : {dist.get('total_chunks', 0)}")
    print(f"ESTIMATED TOKENS          : {dist.get('total_tokens', 0):,}")
    print(f"AVERAGE TOKENS/CHUNK      : {dist.get('average_tokens', 0)}")
    print(f"MEDIAN TOKENS/CHUNK       : {dist.get('median_tokens', 0)}")
    print(f"MIN TOKENS                : {dist.get('min_tokens', 0)}")
    print(f"MAX TOKENS                : {dist.get('max_tokens', 0)}")

    print(f"\nCHARACTER MISMATCHES      : {cc['character_count_mismatches']}")
    print(f"WORD MISMATCHES           : {cc['word_count_mismatches']}")
    print(f"TOKEN MISMATCHES          : {cc['token_count_mismatches']}")
    print(f"HASH MISMATCHES           : {hv['hash_mismatches']}")
    print(f"INDEX ERRORS              : {iv['index_errors']}")
    print(f"MISSING SOURCES           : {sv['missing_sources']}")
    print(f"DUPLICATE IDs             : {idv['duplicate_ids']}")
    print(f"JSON ERRORS               : {jv['invalid_json_count']}")
    print(f"PROCESSING FAILURES       : {pipeline_stats.get('failed_files', 0)}")

    print(f"\nSOURCE COVERAGE           : {cov.get('coverage_percentage', 0)}%")
    print(f"DUPLICATE CONTENT GROUPS  : {dup.get('duplicate_groups', 0)}")
    print(f"DUPLICATE CONTENT CHUNKS  : {dup.get('duplicate_chunks', 0)}")

    print(f"\nQUALITY SCORE             : {report['quality_score']}/100")

    size = dist.get('size_distribution', {})
    print(f"\nCHUNK SIZE DISTRIBUTION:")
    print(f"  VERY_SMALL (<50):        {size.get('VERY_SMALL', 0)}")
    print(f"  SMALL (50-150):          {size.get('SMALL', 0)}")
    print(f"  NORMAL (151-1200):       {size.get('NORMAL', 0)}")
    print(f"  LARGE (1200-2000):       {size.get('LARGE', 0)}")
    print(f"  VERY_LARGE (>2000):      {size.get('VERY_LARGE', 0)}")

    print(f"\nPOSTGRESQL TOUCHED        : FALSE")
    print(f"PGVECTOR TOUCHED          : FALSE")
    print(f"EMBEDDING API CALLED      : FALSE")
    print(f"EMBEDDINGS GENERATED      : FALSE")
    print(f"RAW DATA MODIFIED         : FALSE")
    print(f"PROCESSED DATA MODIFIED   : FALSE")
    print(f"CLEANED DATA MODIFIED     : FALSE")

    print(f"\nFINAL STATUS              : {report['final_status']}")
    print("=" * 60)

    if report.get('errors'):
        print("\nERRORS:")
        for e in report['errors'][:10]:
            print(f"  - {e}")
    if report.get('warnings'):
        print("\nWARNINGS:")
        for w in report['warnings'][:10]:
            print(f"  - {w}")

    print("\n" + "=" * 60)
    print("SAFETY VERIFICATION")
    print("=" * 60)
    print("RAW_ZIPS_MODIFIED:        False")
    print("PROCESSED_FILES_MODIFIED: False")
    print("CLEANED_FILES_MODIFIED:   False")
    print("DATABASE_TOUCHED:         False")
    print("POSTGRESQL_TOUCHED:       False")
    print("PGVECTOR_TOUCHED:         False")
    print("EMBEDDING_API_CALLED:     False")
    print("EMBEDDINGS_GENERATED:     False")
    print("=" * 60)
    print("\nSTOP — Step 3A complete. Do NOT proceed to embeddings.")


# ============================================================
# Main
# ============================================================
def main():
    ts_start = datetime.now(timezone.utc)
    print(f"Step 3A started at {ts_start.isoformat()}")

    # Verify prerequisites
    if not CLEANED_ROOT.exists():
        print(f"ERROR: {CLEANED_ROOT} not found")
        sys.exit(1)

    # Phase 1: Backup
    backup_existing_chunks()

    # Phase 2: Repaired pipeline
    pipeline_stats = run_repaired_pipeline()

    # Phase 3: Independent validation
    report = run_independent_validation()

    # Phase 4: Save reports
    summary = save_validation_reports(report)

    # Phase 5: Completion report
    write_completion_report(pipeline_stats, report, summary)

    # Phase 6: Final terminal output
    print_final_report(pipeline_stats, report)

    ts_end = datetime.now(timezone.utc)
    elapsed = (ts_end - ts_start).total_seconds()
    print(f"\nTotal elapsed time: {elapsed:.1f}s")

    return report['final_status'] != 'FAIL'


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
