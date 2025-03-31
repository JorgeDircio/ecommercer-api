import httpx

class HttpService:
    def __init__(self):
        self.client = httpx.AsyncClient()

    async def post(self, url: str, payload: dict, headers: dict = None, use_json: bool = True) -> dict:
        try:
            if use_json:
                response = await self.client.post(url, json=payload, headers=headers)
            else:
                response = await self.client.post(url, data=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            print("[HTTPStatusError]", e.response.text)
            return {"status": e.response.status_code, "error": e.response.text}
        except httpx.RequestError as e:
            print("[RequestError]", str(e))
            return {"error": str(e)}

    async def get(self, url: str, headers: dict = None) -> dict:
        try:
            response = await self.client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            return {"status": e.response.status_code, "error": e.response.text}
        except httpx.RequestError as e:
            return {"error": str(e)}
