from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):
    stripe_is_active: bool = False
    stripe_client_id: str | None = None
    stripe_oauth_redirect: str | None = None

    BLUMON_USERNAME: str
    BLUMON_RAW_PASSWORD: str
    URL_API_BLUMON_PAY: str
    URL_API_TOKEN: str
    BLUMON_CLIENT_ID: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore"
    )


settings = Settings()
