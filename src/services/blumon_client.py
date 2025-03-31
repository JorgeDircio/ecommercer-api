import time
from src.config import settings
from src.utils.generate_hash import generate_sha256_hash
from src.services.httpClient import HttpService

class BlumonPayClient:
    def __init__(self):
        self.token = None
        self.token_expires_at = 0
        self.http = HttpService()

    async def _get_token(self):
        data = {
            "grant_type": "password",
            "username": settings.BLUMON_USERNAME,
            "password": generate_sha256_hash(settings.BLUMON_RAW_PASSWORD),
            "scope": "read write"
        }
        headers = {
            "Authorization": f"Basic {settings.BLUMON_CLIENT_ID}",
            "Content-Type": "application/x-www-form-urlencoded"
		}
        response = await self.http.post(settings.URL_API_TOKEN, data, headers, use_json=False)
        
        self.token = response["access_token"]
        self.token_expires_at = int(time.time()) + response["expires_in"] - 60
        return self.token

    async def _ensure_token(self):
        if not self.token or time.time() >= self.token_expires_at:
            await self._get_token()

    async def post(self, endpoint: str, payload: dict):
        await self._ensure_token()
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        endpoint = f"{settings.URL_API_BLUMON_PAY}/{endpoint}"
        return await self.http.post(endpoint, payload, headers)
