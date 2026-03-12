from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Application
    APP_NAME: str = os.getenv("APP_NAME")
    APP_ENV: str = os.getenv("APP_ENV")
    DEBUG: bool = os.getenv("DEBUG")

    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    # GitHub
    GITHUB_TOKEN: str = os.getenv("GITHUB_TOKEN")
    GITHUB_API_BASE_URL: str = os.getenv("GITHUB_API_BASE_URL")

    # Security
    # Set a strong random string in production. If empty, auth is disabled (local dev only).
    API_KEY: str = os.getenv("API_KEY")

    # LLM (OpenAI-compatible)
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    OPENAI_BASE_URL: str = os.getenv("OPENAI_BASE_URL")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL")


settings = Settings()
