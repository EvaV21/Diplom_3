import allure

from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators as F
from utils.urls import FEED_URL


class FeedPage(BasePage):

    @allure.step("Открыть страницу ленты заказов")
    def open_feed(self):
        self.open(FEED_URL)
        self.is_visible(F.FEED_HEADER)

    @allure.step("Получить 'Выполнено за все время'")
    def get_total_all_time(self) -> int:
        return int(self.text(F.TOTAL_ALL_TIME))

    @allure.step("Получить 'Выполнено за сегодня'")
    def get_total_today(self) -> int:
        return int(self.text(F.TOTAL_TODAY))

    @allure.step("Получить номера заказов в разделе 'В работе'")
    def get_in_progress_numbers(self) -> list[str]:
        elements = self.find_elements(F.IN_PROGRESS_NUMBERS)
        numbers = []

        for element in elements:
            value = element.text.strip()
            if value:
                numbers.append(value.lstrip("0") or "0")

        return numbers

    @allure.step("Обновить ленту заказов")
    def refresh_feed(self):
        self.refresh_page()

    @allure.step("Дождаться увеличения счетчика 'Выполнено за все время'")
    def wait_total_all_time_increased(self, before_value: int):
        self.wait_number_increases(F.TOTAL_ALL_TIME, before_value)

    @allure.step("Дождаться увеличения счетчика 'Выполнено за сегодня'")
    def wait_total_today_increased(self, before_value: int):
        self.wait_number_increases(F.TOTAL_TODAY, before_value)

    @allure.step("Дождаться появления номера заказа в разделе 'В работе'")
    def wait_order_number_in_progress(self, order_number: str) -> bool:
        return self.wait_until_true(
            lambda: self.has_text_in_elements(F.IN_PROGRESS_NUMBERS, order_number)
        )