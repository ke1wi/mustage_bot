from typing import Optional

from pydantic import AnyUrl, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DEVELOPMENT: bool = True
    DEBUG: bool = True
    NGROK_AUTHTOKEN: Optional[SecretStr] = None

    TOKEN: SecretStr
    TELEGRAM_SECRET: SecretStr
    BASE_URL: AnyUrl = AnyUrl("http://localhost:8000")
    API_URL: AnyUrl
    WEBHOOK_PATH: str = "webhook"

    @property
    def WEBHOOK_URL(self) -> str:
        return f"{self.BASE_URL}{self.WEBHOOK_PATH}"

    model_config = SettingsConfigDict(env_file=(".env", "stack.env"), env_file_encoding="utf-8", extra="ignore")


settings = Settings()  # type: ignore[call-arg]
