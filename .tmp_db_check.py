"""Secret-safe database connectivity check."""

from sqlalchemy import text

from database.connection import engine


try:
	with engine.connect() as connection:
		connection.execute(text("SELECT 1"))
	print("DATABASE_CONNECTION: True")
except Exception:
	print("DATABASE_CONNECTION: False")
