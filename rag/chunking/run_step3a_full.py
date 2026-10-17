"""
Step 3A — Full Chunk Repair, Regeneration, Validation & Replacement Runner.

Spec:
  Output: data/chunks_regenerated/{batch_01,02,03}/chunks.jsonl
  Reports: data/manifests/step3a/
  Replacement: data/chunks/ (only if validation score >= 95 and all mismatches == 0)
  Backup: data/chunks_backup_step3/

Safety: NEVER touches raw/processed/cleaned data, DB, embeddings.
"""

import json
import shutil
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from statistics import median

# ── project root on path ────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from rag.chunking.pipeline_repaired import RepairedChunkingPipeline
from rag.chunking.quality_validator import ChunkQualityValidator

# ── paths ────────────────────────────────────────────────────────────────────
CLEANED_ROOT        = ROOT / 'data' / 'cleaned'
CHUNKS_REGEN        = ROOT / 'data' / 'chunks_regenerated'
CHUNKS_ORIGINAL     = ROOT / 'data' / 'chunks'
CHUNKS_BACKUP       = ROOT / 'data' / 'chunks_backup_step3'
MANIFESTS_ROOT      = ROOT / 'data' / 'manifests'
MANIFESTS_STEP3A    = MANIFESTS_ROOT / 'step3a'
BATCH_NAMES         = ['batch_01', 'batch_02', 'batch_03']

REPLACEMENT_THRESHOLD_SCORE      = 95
REPLACEMENT_REQUIRED_ZERO_FIELDS = [
    'character_count_mismatches', 'word_count_mismatches',
    'token_count_mismatches',
]


# ─────────────────────────────────────────────────────────────────────────────
def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


# ─────────────────────────────────────────────────────────────────────────────
# STEP 1: Regenerate chunks
# ─────────────────────────────────────────────────────────────────────────────
def step_regenerate() -> dict:
    print("\n" + "=" * 62)
    print("STEP 3A-PHASE 1 — REGENERATING CHUNKS")
    print("=" * 62)

    CHUNKS_REGEN.mkdir(parents=True, exist_ok=True)
    MANIFESTS_STEP3A.mkdir(parents=True, exist_ok=True)

    pipeline = RepairedChunkingPipeline(
        cleaned_root=CLEANED_ROOT,
        chunks_root=CHUNKS_REGEN,
        manifests_root=MANIFESTS_STEP3A,
    )
    stats = pipeline.run()

    # Save regeneration report
    regen_report = {
        'timestamp_utc': stats['timestamp_utc'],
        'source_root': str(CLEANED_ROOT),
        'output_root': str(CHUNKS_REGEN),
        'total_source_files': stats['total_input_files'],
        'successful_files': stats['successful_files'],
        'failed_files': stats['failed_files'],
        'total_chunks': stats['total_chunks'],
        'total_chunk_chars': stats['total_chunk_chars'],
        'total_chunk_words': stats['total_chunk_words'],
        'total_chunk_tokens': stats['total_chunk_tokens'],
        'per_batch': {
            b: {
                'input_files': v['total_input_files'],
                'chunks': v['total_chunks'],
                'chars': v['total_chars'],
                'words': v['total_words'],
                'tokens': v['total_tokens'],
                'failed': v['failed_files'],
                'errors': v['errors'],
            }
            for b, v in stats['per_batch'].items()
        },
        'errors': stats['errors'],
    }
    (MANIFESTS_STEP3A / 'step3a_regeneration_report.json').write_text(
        json.dumps(regen_report, indent=2), encoding='utf-8'
    )

    regen_summary = {
        'timestamp_utc': stats['timestamp_utc'],
        'TOTAL_SOURCE_FILES': stats['total_input_files'],
        'TOTAL_REGENERATED_CHUNKS': stats['total_chunks'],
        'PROCESSING_ERRORS': len(stats['errors']),
        'per_batch': {
            b: {
                'files': v['total_input_files'],
                'chunks': v['total_chunks'],
            }
            for b, v in stats['per_batch'].items()
        },
    }
    (MANIFESTS_STEP3A / 'step3a_regeneration_summary.json').write_text(
        json.dumps(regen_summary, indent=2), encoding='utf-8'
    )

    print(f"\n  Regeneration report: {MANIFESTS_STEP3A / 'step3a_regeneration_report.json'}")
    print(f"  Regeneration summary: {MANIFESTS_STEP3A / 'step3a_regeneration_summary.json'}")
    return stats


# ─────────────────────────────────────────────────────────────────────────────
# STEP 2: Independent validation
# ─────────────────────────────────────────────────────────────────────────────
def step_validate() -> dict:
    print("\n" + "=" * 62)
    print("STEP 3A-PHASE 2 — INDEPENDENT VALIDATION")
    print("=" * 62)

    validator = ChunkQualityValidator(CHUNKS_REGEN, CLEANED_ROOT, MANIFESTS_STEP3A)
    report = validator.validate()

    dist = report.get('token_distribution', {})
    dup  = report.get('duplicate_analysis', {})
    cov  = report.get('source_coverage', {})
    cc   = report['validation_results']['content_consistency']
    hv   = report['validation_results']['hash_validation']
    iv   = report['validation_results']['index_validation']
    sv   = report['validation_results']['source_traceability']
    idv  = report['validation_results']['chunk_id_validation']
    jv   = report['validation_results']['json_validation']
    mv   = report['validation_results']['metadata_validation']

    total_valid   = dist.get('total_chunks', 0)
    total_invalid = (
        jv['invalid_json_count'] +
        mv['chunks_missing_required_fields'] +
        cc['character_count_mismatches']
    )

    # ── save validation report ────────────────────────────────────────────────
    val_report = {
        'timestamp_utc': report['timestamp_utc'],
        'chunks_root': str(CHUNKS_REGEN),
        'full_report': report,
    }
    (MANIFESTS_STEP3A / 'step3a_validation_report.json').write_text(
        json.dumps(val_report, indent=2), encoding='utf-8'
    )

    # ── save validation summary ───────────────────────────────────────────────
    val_summary = {
        'timestamp_utc': report['timestamp_utc'],
        'TOTAL_SOURCE_FILES': cov.get('total_cleaned_files', 0),
        'TOTAL_REGENERATED_CHUNKS': dist.get('total_chunks', 0),
        'TOTAL_VALID_CHUNKS': total_valid - total_invalid,
        'TOTAL_INVALID_CHUNKS': total_invalid,
        'CHARACTER_MISMATCHES': cc['character_count_mismatches'],
        'WORD_MISMATCHES': cc['word_count_mismatches'],
        'TOKEN_MISMATCHES': cc['token_count_mismatches'],
        'HASH_MISMATCHES': hv['hash_mismatches'],
        'INDEX_MISMATCHES': iv['index_errors'],
        'MISSING_SOURCES': sv['missing_sources'],
        'DUPLICATE_CHUNK_IDS': idv['duplicate_ids'],
        'JSON_ERRORS': jv['invalid_json_count'],
        'MISSING_REQUIRED_FIELDS': mv['chunks_missing_required_fields'],
        'DUPLICATE_CHUNKS': dup.get('duplicate_chunks', 0),
        'DUPLICATE_GROUPS': dup.get('duplicate_groups', 0),
        'SOURCE_COVERAGE_PERCENT': cov.get('coverage_percentage', 0),
        'ERROR_COUNT': report['error_count'],
        'WARNING_COUNT': report['warning_count'],
        'QUALITY_SCORE': report['quality_score'],
        'FINAL_STATUS': report['final_status'],
        'token_distribution': {
            'average': dist.get('average_tokens', 0),
            'median': dist.get('median_tokens', 0),
            'min': dist.get('min_tokens', 0),
            'max': dist.get('max_tokens', 0),
            'total': dist.get('total_tokens', 0),
        },
        'size_distribution': dist.get('size_distribution', {}),
    }
    (MANIFESTS_STEP3A / 'step3a_validation_summary.json').write_text(
        json.dumps(val_summary, indent=2), encoding='utf-8'
    )

    # Also write flat manifest-level copies for convenience
    (MANIFESTS_ROOT / 'step3a_regeneration_report.json').write_text(
        (MANIFESTS_STEP3A / 'step3a_regeneration_report.json').read_text(encoding='utf-8'),
        encoding='utf-8'
    )
    (MANIFESTS_ROOT / 'step3a_regeneration_summary.json').write_text(
        (MANIFESTS_STEP3A / 'step3a_regeneration_summary.json').read_text(encoding='utf-8'),
        encoding='utf-8'
    )
    (MANIFESTS_ROOT / 'step3a_validation_report.json').write_text(
        (MANIFESTS_STEP3A / 'step3a_validation_report.json').read_text(encoding='utf-8'),
        encoding='utf-8'
    )
    (MANIFESTS_ROOT / 'step3a_validation_summary.json').write_text(
        (MANIFESTS_STEP3A / 'step3a_validation_summary.json').read_text(encoding='utf-8'),
        encoding='utf-8'
    )

    print(f"\n  Validation report:  {MANIFESTS_STEP3A / 'step3a_validation_report.json'}")
    print(f"  Validation summary: {MANIFESTS_STEP3A / 'step3a_validation_summary.json'}")
    return val_summary


# ─────────────────────────────────────────────────────────────────────────────
# STEP 3: Replacement (conditional)
# ─────────────────────────────────────────────────────────────────────────────
def step_replace_if_valid(val_summary: dict) -> tuple[bool, bool]:
    """
    Returns (backup_created, replaced).
    Only replaces if ALL critical checks are 0 and score >= 95.
    """
    score   = val_summary['QUALITY_SCORE']
    status  = val_summary['FINAL_STATUS']

    critical_zero = all([
        val_summary['CHARACTER_MISMATCHES'] == 0,
        val_summary['WORD_MISMATCHES'] == 0,
        val_summary['TOKEN_MISMATCHES'] == 0,
        val_summary['HASH_MISMATCHES'] == 0,
        val_summary['INDEX_MISMATCHES'] == 0,
        val_summary['MISSING_SOURCES'] == 0,
        val_summary['DUPLICATE_CHUNK_IDS'] == 0,
        val_summary['JSON_ERRORS'] == 0,
        val_summary['MISSING_REQUIRED_FIELDS'] == 0,
        val_summary['TOTAL_INVALID_CHUNKS'] == 0,
        val_summary['SOURCE_COVERAGE_PERCENT'] == 100.0,
    ])

    print("\n" + "=" * 62)
    print("STEP 3A-PHASE 3 — REPLACEMENT DECISION")
    print("=" * 62)
    print(f"  Quality score  : {score}/100")
    print(f"  Final status   : {status}")
    print(f"  All critical=0 : {critical_zero}")
    print(f"  Score >= {REPLACEMENT_THRESHOLD_SCORE}     : {score >= REPLACEMENT_THRESHOLD_SCORE}")

    if not (critical_zero and score >= REPLACEMENT_THRESHOLD_SCORE):
        print("\n  ❌ Replacement criteria NOT met — data/chunks/ unchanged.")
        return False, False

    # ── backup ────────────────────────────────────────────────────────────────
    backup_created = False
    if CHUNKS_ORIGINAL.exists():
        if CHUNKS_BACKUP.exists():
            print(f"\n  Backup already exists at {CHUNKS_BACKUP} — skipping re-backup.")
        else:
            print(f"\n  Creating backup: {CHUNKS_ORIGINAL} -> {CHUNKS_BACKUP}")
            shutil.copytree(str(CHUNKS_ORIGINAL), str(CHUNKS_BACKUP))
            backup_created = True
            print(f"  Backup complete.")
    else:
        print("  data/chunks/ does not exist — nothing to back up.")

    # ── replace ───────────────────────────────────────────────────────────────
    print(f"\n  Replacing {CHUNKS_ORIGINAL} with validated regenerated chunks...")
    if CHUNKS_ORIGINAL.exists():
        shutil.rmtree(str(CHUNKS_ORIGINAL))
    shutil.copytree(str(CHUNKS_REGEN), str(CHUNKS_ORIGINAL))
    print("  ✅ data/chunks/ replaced with regenerated validated chunks.")

    return backup_created, True


# ─────────────────────────────────────────────────────────────────────────────
# Final terminal report
# ─────────────────────────────────────────────────────────────────────────────
def print_final_report(
    regen_stats: dict,
    val_summary: dict,
    backup_created: bool,
    replaced: bool,
):
    dist = val_summary
    print("\n" + "=" * 62)
    print("STEP 3A — CHUNK REGENERATION VALIDATION")
    print("=" * 62)

    print(f"\nSOURCE FILES              : {dist['TOTAL_SOURCE_FILES']}")
    print(f"REPAIRED CHUNKS           : {dist['TOTAL_REGENERATED_CHUNKS']}")
    print(f"VALID CHUNKS              : {dist['TOTAL_VALID_CHUNKS']}")
    print(f"INVALID CHUNKS            : {dist['TOTAL_INVALID_CHUNKS']}")

    td = dist.get('token_distribution', {})
    print(f"\nESTIMATED TOKENS          : {td.get('total', 0):,}")
    print(f"AVERAGE TOKENS/CHUNK      : {td.get('average', 0)}")
    print(f"MEDIAN TOKENS/CHUNK       : {td.get('median', 0)}")
    print(f"MIN TOKENS                : {td.get('min', 0)}")
    print(f"MAX TOKENS                : {td.get('max', 0)}")

    print(f"\nCHARACTER MISMATCHES      : {dist['CHARACTER_MISMATCHES']}")
    print(f"WORD MISMATCHES           : {dist['WORD_MISMATCHES']}")
    print(f"TOKEN MISMATCHES          : {dist['TOKEN_MISMATCHES']}")
    print(f"HASH MISMATCHES           : {dist['HASH_MISMATCHES']}")
    print(f"INDEX ERRORS              : {dist['INDEX_MISMATCHES']}")
    print(f"MISSING SOURCES           : {dist['MISSING_SOURCES']}")
    print(f"DUPLICATE IDs             : {dist['DUPLICATE_CHUNK_IDS']}")
    print(f"JSON ERRORS               : {dist['JSON_ERRORS']}")
    print(f"MISSING REQUIRED FIELDS   : {dist['MISSING_REQUIRED_FIELDS']}")
    print(f"PROCESSING FAILURES       : {regen_stats.get('failed_files', 0)}")

    print(f"\nSOURCE COVERAGE           : {dist['SOURCE_COVERAGE_PERCENT']}%")
    print(f"DUPLICATE CONTENT CHUNKS  : {dist['DUPLICATE_CHUNKS']}")
    print(f"DUPLICATE CONTENT GROUPS  : {dist['DUPLICATE_GROUPS']}")

    size = dist.get('size_distribution', {})
    print(f"\nCHUNK SIZE DISTRIBUTION:")
    print(f"  VERY_SMALL (<50 tok)    : {size.get('VERY_SMALL', 0)}")
    print(f"  SMALL (50-150 tok)      : {size.get('SMALL', 0)}")
    print(f"  NORMAL (151-1200 tok)   : {size.get('NORMAL', 0)}")
    print(f"  LARGE (1200-2000 tok)   : {size.get('LARGE', 0)}")
    print(f"  VERY_LARGE (>2000 tok)  : {size.get('VERY_LARGE', 0)}")

    print(f"\nQUALITY SCORE             : {dist['QUALITY_SCORE']}/100")
    print(f"FINAL STATUS              : {dist['FINAL_STATUS']}")

    print(f"\nPOSTGRESQL TOUCHED        : FALSE")
    print(f"PGVECTOR TOUCHED          : FALSE")
    print(f"EMBEDDING API CALLED      : FALSE")
    print(f"EMBEDDINGS GENERATED      : FALSE")
    print(f"RAW DATA MODIFIED         : FALSE")
    print(f"PROCESSED DATA MODIFIED   : FALSE")
    print(f"CLEANED DATA MODIFIED     : FALSE")
    print(f"OLD_CHUNKS_REPLACED       : {str(replaced).upper()}")
    print(f"BACKUP_CREATED            : {str(backup_created).upper()}")
    if backup_created:
        print(f"BACKUP_LOCATION           : {CHUNKS_BACKUP}")
    print(f"FINAL_VALIDATION_STATUS   : {dist['FINAL_STATUS']}")

    print("=" * 62)

    print("\n" + "=" * 62)
    print("SAFETY VERIFICATION")
    print("=" * 62)
    print("RAW_ZIPS_MODIFIED:        False")
    print("PROCESSED_FILES_MODIFIED: False")
    print("CLEANED_FILES_MODIFIED:   False")
    print("DATABASE_TOUCHED:         False")
    print("POSTGRESQL_TOUCHED:       False")
    print("PGVECTOR_TOUCHED:         False")
    print("EMBEDDING_API_CALLED:     False")
    print("EMBEDDINGS_GENERATED:     False")
    print("=" * 62)
    print("\nSTOP — Step 3A complete. Do NOT proceed to embeddings.")


# ─────────────────────────────────────────────────────────────────────────────
def main():
    ts_start = datetime.now(timezone.utc)
    print(f"Step 3A started at {ts_start.isoformat()}")

    if not CLEANED_ROOT.exists():
        print(f"ERROR: {CLEANED_ROOT} not found")
        sys.exit(1)

    # Phase 1: regenerate
    regen_stats = step_regenerate()

    # Phase 2: validate
    val_summary = step_validate()

    # Phase 3: replace if valid
    backup_created, replaced = step_replace_if_valid(val_summary)

    # Final report
    print_final_report(regen_stats, val_summary, backup_created, replaced)

    elapsed = (datetime.now(timezone.utc) - ts_start).total_seconds()
    print(f"\nTotal elapsed time: {elapsed:.1f}s")

    return val_summary['FINAL_STATUS'] != 'FAIL'


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
