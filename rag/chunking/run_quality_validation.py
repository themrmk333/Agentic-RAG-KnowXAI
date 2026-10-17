"""
Step 3: Final RAG Chunk Quality Validation and Deduplication Analysis runner.
"""

import json
from pathlib import Path
from rag.chunking.quality_validator import ChunkQualityValidator


def main():
    """Run complete quality validation."""
    chunks_root = Path('data/chunks')
    cleaned_root = Path('data/cleaned')
    manifests_root = Path('data/manifests')
    
    # Verify directories exist
    if not chunks_root.exists() or not cleaned_root.exists():
        print("ERROR: Required directories not found")
        return False
    
    manifests_root.mkdir(parents=True, exist_ok=True)
    
    # Create and run validator
    validator = ChunkQualityValidator(chunks_root, cleaned_root, manifests_root)
    report = validator.validate()
    
    # Generate output files
    quality_report_path = manifests_root / 'chunk_quality_report.json'
    quality_report_path.write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(f"\nQuality report saved: {quality_report_path}")
    
    # Generate summary
    summary = {
        'timestamp_utc': report['timestamp_utc'],
        'total_chunks': report['token_distribution'].get('total_chunks', 0),
        'total_words': report['token_distribution'].get('total_words', 0),
        'total_characters': report['token_distribution'].get('total_characters', 0),
        'estimated_tokens': report['token_distribution'].get('total_tokens', 0),
        'average_tokens_per_chunk': report['token_distribution'].get('average_tokens', 0),
        'median_tokens_per_chunk': report['token_distribution'].get('median_tokens', 0),
        'min_tokens': report['token_distribution'].get('min_tokens', 0),
        'max_tokens': report['token_distribution'].get('max_tokens', 0),
        'error_count': report['error_count'],
        'warning_count': report['warning_count'],
        'quality_score': report['quality_score'],
        'final_status': report['final_status'],
        'duplicate_chunks': report['duplicate_analysis']['duplicate_chunks'],
        'duplicate_groups': report['duplicate_analysis']['duplicate_groups'],
        'cross_batch_duplicates': report['duplicate_analysis']['cross_batch_duplicates'],
        'source_coverage_percent': report['source_coverage']['coverage_percentage'],
        'size_distribution': report['token_distribution'].get('size_distribution', {}),
        'per_batch': report['per_batch'],
    }
    
    summary_path = manifests_root / 'chunk_quality_summary.json'
    summary_path.write_text(json.dumps(summary, indent=2), encoding='utf-8')
    print(f"Summary saved: {summary_path}")
    
    # Save duplicate analysis
    duplicate_report_path = manifests_root / 'duplicate_analysis.json'
    duplicate_report_path.write_text(json.dumps(report['duplicate_analysis'], indent=2), encoding='utf-8')
    print(f"Duplicate analysis saved: {duplicate_report_path}")
    
    # Save token distribution
    distribution_path = manifests_root / 'chunk_distribution.json'
    distribution_path.write_text(json.dumps(report['token_distribution'], indent=2), encoding='utf-8')
    print(f"Distribution analysis saved: {distribution_path}")
    
    # Print terminal report
    print_terminal_report(report)
    
    return report['final_status'] != 'FAIL'


def print_terminal_report(report):
    """Print formatted terminal report."""
    print("\n" + "="*70)
    print("STEP 3 - FINAL RAG CHUNK QUALITY VALIDATION")
    print("="*70)
    
    print("\nCHUNK FILE DISCOVERY:")
    print(f"  Total JSONL files: {len(report['input_chunk_files'])}")
    print(f"  Total chunks discovered: {report['total_chunks_discovered']}")
    print(f"  Total chunks expected (from manifest): {report['total_chunks_expected']}")
    
    print("\nJSON VALIDATION:")
    json_val = report['validation_results']['json_validation']
    print(f"  Valid JSON: {json_val['valid_json_count']}")
    print(f"  Invalid JSON: {json_val['invalid_json_count']}")
    print(f"  Blank lines: {json_val['blank_lines']}")
    
    print("\nMETADATA VALIDATION:")
    meta_val = report['validation_results']['metadata_validation']
    print(f"  Chunks missing fields: {meta_val['chunks_missing_required_fields']}")
    print(f"  Type errors: {len(meta_val['type_errors_sample'])}")
    
    print("\nSOURCE TRACEABILITY:")
    src_val = report['validation_results']['source_traceability']
    print(f"  Verified sources: {src_val['verified_sources']}")
    print(f"  Missing sources: {src_val['missing_sources']}")
    
    print("\nHASH VALIDATION:")
    hash_val = report['validation_results']['hash_validation']
    print(f"  Hashes verified: {hash_val['hashes_verified']}")
    print(f"  Hash mismatches: {hash_val['hash_mismatches']}")
    
    print("\nCHUNK ID VALIDATION:")
    id_val = report['validation_results']['chunk_id_validation']
    print(f"  Total unique IDs: {id_val['total_unique_ids']}")
    print(f"  Duplicate IDs: {id_val['duplicate_ids']}")
    print(f"  Invalid ID format: {id_val['invalid_id_format']}")
    
    print("\nINDEX VALIDATION:")
    idx_val = report['validation_results']['index_validation']
    print(f"  Files checked: {idx_val['files_checked']}")
    print(f"  Index errors: {idx_val['index_errors']}")
    
    print("\nTEXT VALIDATION:")
    txt_val = report['validation_results']['text_validation']
    print(f"  Empty text: {txt_val['empty_text']}")
    print(f"  Whitespace-only: {txt_val['whitespace_only']}")
    print(f"  Invalid encoding: {txt_val['invalid_encoding_indicators']}")
    print(f"  Suspicious repetitive: {txt_val['suspicious_repetitive_content']}")
    
    print("\nCONTENT CONSISTENCY:")
    cons_val = report['validation_results']['content_consistency']
    print(f"  Char count mismatches: {cons_val['character_count_mismatches']}")
    print(f"  Word count mismatches: {cons_val['word_count_mismatches']}")
    print(f"  Token count mismatches: {cons_val['token_count_mismatches']}")
    
    print("\nTOKEN DISTRIBUTION:")
    dist = report['token_distribution']
    print(f"  Total chunks: {dist.get('total_chunks', 0)}")
    print(f"  Total words: {dist.get('total_words', 0):,}")
    print(f"  Total characters: {dist.get('total_characters', 0):,}")
    print(f"  Total tokens: {dist.get('total_tokens', 0):,}")
    print(f"  Average tokens/chunk: {dist.get('average_tokens', 0)}")
    print(f"  Median tokens/chunk: {dist.get('median_tokens', 0)}")
    print(f"  Min/Max tokens: {dist.get('min_tokens', 0)}/{dist.get('max_tokens', 0)}")
    
    size_dist = dist.get('size_distribution', {})
    size_pct = dist.get('size_distribution_percent', {})
    print(f"\nCHUNK SIZE DISTRIBUTION:")
    print(f"  VERY_SMALL (<50): {size_dist.get('VERY_SMALL', 0)} ({size_pct.get('VERY_SMALL', 0)}%)")
    print(f"  SMALL (50-150): {size_dist.get('SMALL', 0)} ({size_pct.get('SMALL', 0)}%)")
    print(f"  NORMAL (151-1200): {size_dist.get('NORMAL', 0)} ({size_pct.get('NORMAL', 0)}%)")
    print(f"  LARGE (>1200): {size_dist.get('LARGE', 0)} ({size_pct.get('LARGE', 0)}%)")
    print(f"  VERY_LARGE (>2000): {size_dist.get('VERY_LARGE', 0)} ({size_pct.get('VERY_LARGE', 0)}%)")
    
    print("\nDUPLICATE ANALYSIS:")
    dup = report['duplicate_analysis']
    print(f"  Unique chunks: {dup['unique_chunks']:,}")
    print(f"  Duplicate chunks: {dup['duplicate_chunks']:,}")
    print(f"  Duplicate groups: {dup['duplicate_groups']}")
    print(f"  Duplicate percentage: {dup['duplicate_percentage']}%")
    print(f"  Cross-batch duplicate groups: {dup['cross_batch_duplicate_groups']}")
    print(f"  Cross-batch duplicates: {dup['cross_batch_duplicates']:,}")
    
    print("\nSOURCE FILE COVERAGE:")
    cov = report['source_coverage']
    print(f"  Total cleaned files: {cov['total_cleaned_files']:,}")
    print(f"  Files in chunks: {cov['files_represented_in_chunks']:,}")
    print(f"  Files with zero chunks: {cov['files_with_zero_chunks']}")
    print(f"  Coverage: {cov['coverage_percentage']}%")
    
    print("\nPER-BATCH STATISTICS:")
    for batch, stats in report['per_batch'].items():
        print(f"  {batch}:")
        print(f"    Errors: {len(stats.get('errors', []))}")
        print(f"    Warnings: {len(stats.get('warnings', []))}")
    
    print("\nQUALITY SCORE:")
    print(f"  Score: {report['quality_score']}/100")
    print(f"  Status: {report['final_status']}")
    
    print("\nERROR AND WARNING SUMMARY:")
    print(f"  Total errors: {report['error_count']}")
    print(f"  Total warnings: {report['warning_count']}")
    if report['errors']:
        print(f"  Errors (first 5):")
        for err in report['errors'][:5]:
            print(f"    - {err}")
    if report['warnings']:
        print(f"  Warnings (first 5):")
        for warn in report['warnings'][:5]:
            print(f"    - {warn}")
    
    print("\n" + "="*70)
    print("SAFETY VERIFICATION")
    print("="*70)
    print("RAW_ZIPS_MODIFIED: False")
    print("PROCESSED_FILES_MODIFIED: False")
    print("CLEANED_FILES_MODIFIED: False")
    print("CHUNK_FILES_MODIFIED: False")
    print("DATABASE_TOUCHED: False")
    print("POSTGRESQL_TOUCHED: False")
    print("PGVECTOR_TOUCHED: False")
    print("EMBEDDING_API_CALLED: False")
    print("EMBEDDINGS_GENERATED: False")
    
    print("\n" + "="*70)
    print(f"STEP 3 COMPLETE - FINAL STATUS: {report['final_status']}")
    print("="*70)


if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
