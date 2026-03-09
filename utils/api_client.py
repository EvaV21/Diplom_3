import random
import string

import allure
import requests

from utils.urls import (
    API_URL,
    REGISTER_ENDPOINT,
    LOGIN_ENDPOINT,
    INGREDIENTS_ENDPOINT,
    ORDERS_ENDPOINT,
)


class StellarApiClient:

    @staticmethod
    def _rand_str(length=10) -> str:
        chars = string.ascii_letters + string.digits
        return "".join(random.choice(chars) for _ in range(length))

    @allure.step("Сгенерировать данные нового пользователя")
    def generate_user_payload(self) -> dict:
        return {
            "email": f"eva_{self._rand_str(8).lower()}@yandex.ru",
            "password": self._rand_str(12),
            "name": f"Eva_{self._rand_str(6)}",
        }

    @allure.step("Зарегистрировать нового пользователя")
    def register_user(self) -> dict:
        payload = self.generate_user_payload()
        response = requests.post(API_URL + REGISTER_ENDPOINT, json=payload)
        response.raise_for_status()
        return payload

    @allure.step("Авторизовать пользователя")
    def login(self, email: str, password: str) -> str:
        response = requests.post(
            API_URL + LOGIN_ENDPOINT,
            json={"email": email, "password": password}
        )
        response.raise_for_status()
        return response.json()["accessToken"]

    @allure.step("Получить список ингредиентов")
    def get_ingredients(self) -> list[str]:
        response = requests.get(API_URL + INGREDIENTS_ENDPOINT)
        response.raise_for_status()
        return [item["_id"] for item in response.json()["data"]]

    @allure.step("Создать заказ через API")
    def create_order(self, ingredients: list[str], token: str) -> str:
        headers = {"Authorization": token}
        response = requests.post(
            API_URL + ORDERS_ENDPOINT,
            json={"ingredients": ingredients},
            headers=headers
        )
        response.raise_for_status()
        return str(response.json()["order"]["number"])