from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Settings for the app which will be populated using .env files, when present."""

    aws_access_key_id: str
    aws_region: str = "eu-west-2"
    aws_secret_access_key: str

    dynamodb_host: str | None = None
    dynamodb_table_name: str = "Cakes"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    return Settings()
