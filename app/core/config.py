from __future__ import annotations
import urllib.parse
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # DB parts (will be read from env or .env)
    DATABASE_HOST: str
    DATABASE_PORT: int = 3306
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str

    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }

    @property
    def DATABASE_URL(self) -> str:
        pw = urllib.parse.quote_plus(self.DATABASE_PASSWORD or "")
        return f"mysql+pymysql://{self.DATABASE_USER}:{pw}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"


settings = Settings()