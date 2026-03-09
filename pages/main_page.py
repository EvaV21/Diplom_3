import allure

from locators.main_page_locators import MainPageLocators as L
from pages.base_page import BasePage
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

    @allure.step("Проверить, что модальное окно ингредиента открыто")
    def is_ingredient_modal_opened(self) -> bool:
        return self.is_visible(L.MODAL) and self.is_visible(L.MODAL_TITLE)

    @allure.step("Закрыть модальное окно ингредиента крестиком")
    def close_ingredient_modal(self):
        self.click_visible(L.MODAL_CLOSE)

    @allure.step("Проверить, что модальное окно ингредиента закрыто")
    def is_ingredient_modal_closed(self) -> bool:
        return self.is_not_visible(L.MODAL)

    @allure.step("Добавить булку в конструктор")
    def add_bun_to_constructor(self):
        self.drag_and_drop(L.FIRST_BUN, L.CONSTRUCTOR_DROP_ZONE)

    @allure.step("Получить значение счетчика булки")
    def get_bun_counter(self) -> int:
        return self.get_counter_value_or_zero(L.FIRST_BUN_COUNTER)

    @allure.step("Дождаться, что счетчик булки равен {value}")
    def wait_bun_counter_equals(self, value: int):
        self.wait_text_equals(L.FIRST_BUN_COUNTER, str(value))

    @allure.step("Проверить, что URL содержит {part}")
    def has_url_part(self, part: str) -> bool:
        return self.current_url_contains(part)