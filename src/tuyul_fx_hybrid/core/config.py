"""Configuration management for TUYUL-FX-HYBRID."""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application settings."""
    
    # API Configuration
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_version: str = "v5.4.0"
    debug: bool = False
    
    # OpenAI/GPT Configuration
    openai_api_key: str
    gpt_model: str = "gpt-4-turbo-preview"
    gpt_max_tokens: int = 4096
    gpt_temperature: float = 0.7
    
    # GitHub Configuration
    github_token: str
    github_knowledge_vault_repo: str
    github_journal_vault_repo: str
    
    # Database Configuration
    database_url: str = "postgresql://user:password@localhost:5432/tuyul_agi"
    
    # Redis Configuration
    redis_url: str = "redis://localhost:6379/0"
    
    # OCR Configuration
    tesseract_path: str = "/usr/bin/tesseract"
    ocr_lang: str = "eng+ind"
    
    # Adaptive Learning Configuration
    learning_rate: float = 0.001
    batch_size: int = 32
    epochs: int = 100
    
    # Security
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # Logging
    log_level: str = "INFO"
    log_file: str = "logs/tuyul-fx-hybrid.log"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
