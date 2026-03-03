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

    @allure.step("Получить номера заказов в 'В работе'")
    def get_in_progress_numbers(self) -> list[str]:
        els = self.driver.find_elements(*F.IN_PROGRESS_NUMBERS)
        nums = []
        for e in els:
            t = e.text.strip()
            if t:
                nums.append(t.lstrip("0") or "0")
        return nums