from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    debug: bool = False
    secret_key: str = Field(default='S#perS3crEt_9999', alias='SECRET_KEY')
    server_address: str = Field(default='http://localhost:8000/', alias='BASE_URL')

    stripe_secret_key: str = Field(default='sk_live_...', alias='STRIPE_SECRET_KEY')
    stripe_publishable_key: str = Field(default='pk_live_...', alias='STRIPE_PUBLISHABLE_KEY')
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
        self.check_stripe()

    def check_stripe(self):
        if self.stripe_secret_key and self.stripe_publishable_key:
            self.stripe_is_active = True

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore"
    )


settings = Settings()
