from pathlib import Path
from collections import Counter
import re
import math

ROOT = Path("data/processed")

TEXT_EXTENSIONS = {
    ".md", ".json", ".csv", ".txt", ".markdown",
    ".html", ".xml", ".yaml", ".yml", ".rtf", ".log"
}

def estimate_tokens(chars):
    return chars / 4

def estimate_pages(words):
    return words / 450

def analyze_folder(folder):
    files = [p for p in folder.rglob("*") if p.is_file()]

    total_chars = 0
    total_words = 0
    total_lines = 0
    text_files = 0
    skipped_files = 0
    ext_counts = Counter()

    for path in files:
        ext = path.suffix.lower()
        ext_counts[ext] += 1

        if ext not in TEXT_EXTENSIONS:
            skipped_files += 1
            continue

        try:
            text = path.read_text(
                encoding="utf-8",
                errors="ignore"
            )
        except Exception:
            skipped_files += 1
            continue

        text_files += 1
        total_chars += len(text)
        total_words += len(re.findall(r"\S+", text))
        total_lines += text.count("\n") + 1

    return {
        "all_files": len(files),
        "text_files": text_files,
        "skipped_files": skipped_files,
        "characters": total_chars,
        "words": total_words,
        "lines": total_lines,
        "tokens": estimate_tokens(total_chars),
        "pages": estimate_pages(total_words),
        "extensions": ext_counts
    }


print("=" * 70)
print("MK INFINITAI DATASET - CONTENT SIZE VALIDATION")
print("=" * 70)
print("Database touched : NO")
print("PostgreSQL        : NO")
print("pgvector          : NO")
print("Embedding API     : NO")
print("Embeddings        : NO")
print()

grand = {
    "files": 0,
    "text_files": 0,
    "chars": 0,
    "words": 0,
    "lines": 0,
    "tokens": 0,
    "pages": 0
}

for batch in ["batch_01", "batch_02", "batch_03"]:

    folder = ROOT / batch

    print("-" * 70)
    print(batch.upper())
    print("-" * 70)

    result = analyze_folder(folder)

    print(f"Files            : {result['all_files']:,}")
    print(f"Text files       : {result['text_files']:,}")
    print(f"Characters       : {result['characters']:,}")
    print(f"Words            : {result['words']:,}")
    print(f"Lines            : {result['lines']:,}")
    print(f"Estimated tokens : {result['tokens']:,.0f}")
    print(f"Estimated pages  : {result['pages']:,.0f}")

    print("\nExtensions:")

    for ext, count in result["extensions"].most_common():
        name = ext if ext else "[no extension]"
        print(f"  {name:12} : {count:,}")

    grand["files"] += result["all_files"]
    grand["text_files"] += result["text_files"]
    grand["chars"] += result["characters"]
    grand["words"] += result["words"]
    grand["lines"] += result["lines"]
    grand["tokens"] += result["tokens"]
    grand["pages"] += result["pages"]


print()
print("=" * 70)
print("COMBINED DATASET RESULT")
print("=" * 70)

print(f"Total files          : {grand['files']:,}")
print(f"Total text files     : {grand['text_files']:,}")
print(f"Total characters     : {grand['chars']:,}")
print(f"Total words          : {grand['words']:,}")
print(f"Estimated tokens     : {grand['tokens']:,.0f}")
print(f"Estimated pages      : {grand['pages']:,.0f}")

print()
print("=" * 70)
print("RAG CHUNK ESTIMATES")
print("=" * 70)

for chunk_size in [300, 500, 800, 1000, 1200]:
    chunks = math.ceil(grand["tokens"] / chunk_size)
    print(
        f"{chunk_size:4} tokens/chunk -> "
        f"approximately {chunks:,} chunks"
    )

print()
print("=" * 70)
print("10,000 PAGE TARGET CHECK")
print("=" * 70)

if grand["pages"] >= 10000:
    print("STATUS: PASS")
    print("Dataset is estimated to contain 10,000+ pages.")
else:
    print("STATUS: BELOW TARGET")
    print(f"Estimated pages: {grand['pages']:,.0f}")
    print(
        f"Pages still needed: "
        f"{10000 - grand['pages']:,.0f}"
    )

print()
print("NOTE:")
print("Page count is an estimate because Markdown, JSON and CSV")
print("files do not have physical pages.")
print("=" * 70)