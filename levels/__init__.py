import os

AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "your-aws-secret-key-here")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
AWS_ACCOUNT_ID = os.getenv("AWS_ACCOUNT_ID", "000000000000")
DB_HOST = os.getenv("DB_HOST", "medvitals-prod.us-east-1.rds.amazonaws.com")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME", "medvitals_prod")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "your-db-password-here")
LLM_ENDPOINT = os.getenv("LLM_ENDPOINT", "https://api.openai.com/v1/chat/completions")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o")
LLM_TIMEOUT = int(os.getenv("LLM_TIMEOUT", "30"))
SESSION_SECRET = os.getenv("SESSION_SECRET", "your-session-secret-here")

__all__ = [
    "AWS_SECRET_ACCESS_KEY",
    "AWS_REGION",
    "AWS_ACCOUNT_ID",
    "DB_HOST",
    "DB_PORT",
    "DB_NAME",
    "DB_USER",
    "DB_PASSWORD",
    "LLM_ENDPOINT",
    "LLM_MODEL",
    "LLM_TIMEOUT",
    "SESSION_SECRET",
]
