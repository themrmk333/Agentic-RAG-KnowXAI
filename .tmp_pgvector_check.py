from sqlalchemy import text
from database.connection import engine

try:
    with engine.connect() as connection:
        result1 = connection.execute(text("SELECT 1")).scalar()
        result2 = connection.execute(
            text("SELECT extname FROM pg_extension WHERE extname = 'vector'")
        ).scalar()

        print("SELECT 1:", result1)
        print("PGVECTOR:", result2)

except Exception as e:
    print("ERROR:", repr(e))
