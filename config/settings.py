"""Typed application settings loaded from environment variables."""

from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import SecretStr, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


PROJECT_ROOT = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    """Runtime configuration for the Agentic RAG application."""

    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    app_name: str = "Agentic-RAG-KnowXAI"
    app_env: Literal["development", "testing", "staging", "production"] = "development"
    debug: bool = False
    port: int = 8000
    cors_origins: list[str] = ["*"]
    llm_provider: Literal["gemini", "openrouter", "nvidia", "mock", "local"] = "local"
    gemini_api_key: SecretStr | None = None
    gemini_model: str = "gemini-2.0-flash"
    gemini_openrouter_model: str = "google/gemini-2.0-flash-001"
    nvidia_api_key: SecretStr | None = None
    nvidia_model: str = "meta/llama-3.1-8b-instruct"
    nvidia_openrouter_model: str = "meta-llama/llama-3.1-8b-instruct"
    nvidia_base_url: str = "https://integrate.api.nvidia.com/v1"
    openrouter_base_url: str = "https://openrouter.ai/api/v1"
    embedding_provider: str = "local"
    embedding_api_key: SecretStr | None = None
    embedding_model: str = "BAAI/bge-small-en-v1.5"
    embedding_base_url: str | None = None
    embedding_dimensions: int = 384
    pgvector_dimensions: int = 384
    database_url: SecretStr | None = None
    db_echo: bool = False
    chroma_persist_directory: Path = PROJECT_ROOT / "data" / "chroma"
    local_llm_base_url: str = "http://localhost:11434/v1"
    local_llm_model: str = "llama3.1"
    jwt_secret_key: SecretStr = SecretStr("mk-infinite-ai-enterprise-secret-key-987654321")
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 1440
    biometric_encryption_key: SecretStr = SecretStr("mk-infinite-biometric-key-32bytes-secret-12345")
    face_similarity_threshold: float = 0.75  # Provisional baseline threshold
    google_client_id: str | None = None

    @model_validator(mode="after")
    def validate_gemini_api_key(self) -> "Settings":
        """Fail clearly when Gemini-backed features have no configured key."""
        if self.llm_provider in ("local", "mock"):
            return self
        if self.gemini_api_key is None or not self.gemini_api_key.get_secret_value().strip():
            raise ValueError("GEMINI_API_KEY must be configured in the environment or .env file")
        return self


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return the cached application settings instance."""
    return Settings()
