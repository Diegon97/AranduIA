"""
Configuración central de la aplicación AranduIA usando Pydantic Settings.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    APP_NAME: str = "AranduIA"
    APP_ENV: str = "development"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True

    # Inferencia IA: "local_rules", "ollama", "external_api"
    LLM_PROVIDER: str = "local_rules"

    # Ollama
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "llama3:8b"

    # API Externa (opcional)
    EXTERNAL_API_URL: str = "https://api.groq.com/openai/v1"
    EXTERNAL_API_KEY: Optional[str] = None
    EXTERNAL_API_MODEL: str = "llama-3.1-8b-instant"

    # Privacidad y Ley N° 7593/2025
    ENFORCE_DATA_MINIMIZATION: bool = True
    LOG_ANONYMOUS_METRICS: bool = False

    # WhatsApp
    WHATSAPP_ENABLED: bool = False
    WHATSAPP_VERIFY_TOKEN: str = "arandu_secret_token"
    WHATSAPP_API_URL: Optional[str] = None
    WHATSAPP_API_TOKEN: Optional[str] = None


settings = Settings()
