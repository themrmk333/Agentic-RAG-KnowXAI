from sqlalchemy import text
from database.connection import engine

with engine.connect() as connection:
    documents = connection.execute(
        text("SELECT COUNT(*) FROM documents")
    ).scalar()

    chunks = connection.execute(
        text("SELECT COUNT(*) FROM document_chunks")
    ).scalar()

    embeddings = connection.execute(
        text("SELECT COUNT(*) FROM document_chunks WHERE embedding IS NOT NULL")
    ).scalar()

    print("Documents =", documents)
    print("Chunks =", chunks)
    print("Embeddings =", embeddings)
