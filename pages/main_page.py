import allure
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as L
from utils.urls import BASE_URL


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main(self):
        self.open(BASE_URL)

        self.is_visible(L.FIRST_BUN)

    @allure.step("Перейти в Конструктор")
    def go_to_constructor(self):
        self.click(L.CONSTRUCTOR_TAB)

    @allure.step("Перейти в Ленту заказов")
    def go_to_feed(self):
        self.click(L.FEED_TAB)

    @allure.step("Открыть первую булку")
    def open_first_bun(self):
        self.click(L.FIRST_BUN)

    @allure.step("Проверить, что модалка ингредиента открылась")
    def assert_ingredient_modal_opened(self):
        self.is_visible(L.MODAL)
        self.is_visible(L.MODAL_TITLE)

    @allure.step("Закрыть модалку ингредиента крестиком")
    def close_ingredient_modal(self):
        self.click_visible(L.MODAL_CLOSE)

    @allure.step("Проверить, что модалка ингредиента закрыта")
    def assert_ingredient_modal_closed(self):
        self.is_not_visible(L.MODAL)

    @allure.step("Добавить булку в конструктор (drag&drop)")
    def add_bun_to_constructor(self):
        self.drag_and_drop(L.FIRST_BUN, L.CONSTRUCTOR_DROP_ZONE)

    @allure.step("Получить счетчик булки")
    def get_bun_counter(self) -> int:
        return int(self.text(L.FIRST_BUN_COUNTER))

    @allure.step("Дождаться, что счетчик булки = {value}")
    def wait_bun_counter_equals(self, value: int):
        self.wait.until(EC.text_to_be_present_in_element(L.FIRST_BUN_COUNTER, str(value)))