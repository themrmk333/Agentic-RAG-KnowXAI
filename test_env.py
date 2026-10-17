"""Secret-safe environment variable verification."""

from dotenv import load_dotenv
import os


load_dotenv()

for variable_name in ("GEMINI_API_KEY", "NVIDIA_API_KEY", "DATABASE_URL"):
    print(f"{variable_name}: {bool(os.getenv(variable_name, '').strip())}")
