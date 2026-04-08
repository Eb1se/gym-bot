import httpx
from httpx import HTTPStatusError, RequestError
from typing import Optional, Dict, Any

class APIClient:
    """
    Клиент для вызова нашего FastAPI из бота.
    """
    def __init__(self, base_url: str = "http://api:8000"):
        self.base_url = base_url
        self.client = httpx.AsyncClient(timeout=10.0)
    
    async def register_user(
            self,
            telegram_id: int,
            username: Optional[str] = None,
            first_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Регистация пользователя через API
        """
        url = f"{self.base_url}/api/v1/users/register"

        payload = {
            "telegram_id": telegram_id,
            "username": username,
            "first_name": first_name
        }

        try:
            response = await self.client.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except HTTPStatusError as e:
            print(f"API ошибка: {e.response.status_code} - {e.response.text}")
            raise
        except RequestError as e:
            print(f"Сервер недоступен: {e}")
            raise

    async def close(self):
        await self.client.aclose()

api_client = APIClient()