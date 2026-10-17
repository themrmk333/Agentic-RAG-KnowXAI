from database.connection import engine
from sqlalchemy import text

with engine.connect() as c:
    version = c.execute(
        text("SELECT extversion FROM pg_extension WHERE extname = 'vector'")
    ).scalar()

    print("pgvector:", version)