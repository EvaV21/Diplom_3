import allure
import time

from pages.feed_page import FeedPage
from utils.api_client import StellarApiClient


@allure.suite("Лента заказов")
class TestFeed:

    @allure.title("При создании нового заказа счётчики 'Выполнено за всё время' и 'за сегодня' увеличиваются")
    def test_counters_increase_after_order(self, driver):
        feed = FeedPage(driver)
        api = StellarApiClient()

        feed.open_feed()
        before_all = feed.get_total_all_time()
        before_today = feed.get_total_today()

        user = api.register_user()
        token = api.login(user["email"], user["password"])
        ids = api.get_ingredients()
        api.create_order(ids[:2], token=token)

        feed.open_feed()
        after_all = feed.get_total_all_time()
        after_today = feed.get_total_today()

        for _ in range(60):
            if after_all >= before_all + 1 and after_today >= before_today + 1:
                break
            time.sleep(1)
            driver.refresh()
            after_all = feed.get_total_all_time()
            after_today = feed.get_total_today()

        assert after_all >= before_all + 1
        assert after_today >= before_today + 1

    @allure.title("После создания заказа его номер появляется в разделе 'В работе'")
    def test_order_number_in_progress(self, driver):
        feed = FeedPage(driver)
        api = StellarApiClient()

        user = api.register_user()
        token = api.login(user["email"], user["password"])
        ids = api.get_ingredients()
        order_number = api.create_order(ids[:2], token=token)
        order_number_norm = order_number.lstrip("0") or "0"

        feed.open_feed()

        for _ in range(60):
            numbers = feed.get_in_progress_numbers()
            if order_number_norm in numbers:
                return
            time.sleep(1)
            driver.refresh()

        assert order_number_norm in feed.get_in_progress_numbers()