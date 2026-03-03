import random
import string
import requests


class StellarApiClient:
    BASE_URL = "https://stellarburgers.education-services.ru/api"

    def _rand_str(self, n=10) -> str:
        chars = string.ascii_letters + string.digits
        return "".join(random.choice(chars) for _ in range(n))

    def register_user(self) -> dict:
        payload = {
            "email": f"eva_{self._rand_str(8).lower()}@yandex.ru",
            "password": self._rand_str(12),
            "name": f"Eva_{self._rand_str(6)}",
        }
        r = requests.post(self.BASE_URL + "/auth/register", json=payload)
        r.raise_for_status()
        return payload

    def login(self, email: str, password: str) -> str:
        r = requests.post(self.BASE_URL + "/auth/login", json={"email": email, "password": password})
        r.raise_for_status()
        return r.json()["accessToken"]  

    def get_ingredients(self) -> list[str]:
        r = requests.get(self.BASE_URL + "/ingredients")
        r.raise_for_status()
        return [i["_id"] for i in r.json()["data"]]

    def create_order(self, ingredients: list[str], token: str) -> str:
        headers = {"Authorization": token}
        r = requests.post(self.BASE_URL + "/orders", json={"ingredients": ingredients}, headers=headers)
        r.raise_for_status()
        data = r.json()
        return str(data["order"]["number"])