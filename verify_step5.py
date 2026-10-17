from database.connection import engine
from sqlalchemy import text, inspect

print("=" * 60)
print("STEP 5 DATABASE STATUS CHECK")
print("=" * 60)

with engine.connect() as conn:

    # 1. Embeddings
    embeddings = conn.execute(
        text("SELECT count(embedding) FROM document_chunks")
    ).scalar()

    # 2. Documents
    documents = conn.execute(
        text("SELECT count(*) FROM documents")
    ).scalar()

    # 3. Chunks
    chunks = conn.execute(
        text("SELECT count(*) FROM document_chunks")
    ).scalar()

    # 4. Missing vectors
    missing = conn.execute(
        text("SELECT count(*) FROM document_chunks WHERE embedding IS NULL")
    ).scalar()

    # 5. pgvector
    pgvector = conn.execute(
        text("SELECT extversion FROM pg_extension WHERE extname = 'vector'")
    ).scalar()

    # 6. Vector dimension
    dimension = conn.execute(
        text("""
        SELECT format_type(atttypid, atttypmod)
        FROM pg_attribute
        WHERE attrelid = 'document_chunks'::regclass
        AND attname = 'embedding'
        """)
    ).scalar()

print(f"Embeddings          : {embeddings}")
print(f"Documents           : {documents}")
print(f"Chunks              : {chunks}")
print(f"Missing embeddings  : {missing}")
print(f"pgvector            : {pgvector}")
print(f"Vector dimension    : {dimension}")

print()
print("Indexes:")

indexes = inspect(engine).get_indexes("document_chunks")

hnsw_found = False

for index in indexes:
    print(f"  - {index['name']}")

    if index["name"] == "ix_document_chunks_embedding_cosine":
        hnsw_found = True
        print("    Type : HNSW")
        print("    Ops  : vector_cosine_ops")

print()
print("=" * 60)
print("FINAL STATUS")
print("=" * 60)

checks = [
    embeddings == 12730,
    documents == 3897,
    chunks == 12730,
    missing == 0,
    pgvector is not None,
    dimension == "vector(384)",
    hnsw_found,
]

if all(checks):
    print("✅ STEP 5 DATABASE: PASS")
    print("✅ 12,730 / 12,730 embeddings")
    print("✅ 3,897 documents linked")
    print("✅ 384-dimensional vectors")
    print(f"✅ pgvector {pgvector}")
    print("✅ HNSW cosine index active")
    print("✅ Missing vectors: 0")
    print("✅ Database integrity: PASS")
else:
    print("❌ STEP 5 DATABASE: CHECK FAILED")

print("=" * 60)