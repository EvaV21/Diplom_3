import allure

from pages.main_page import MainPage
from utils.urls import BASE_URL, FEED_URL


@allure.suite("Основная функциональность")
class TestMainFunctionality:

    @allure.title("Переход по клику на раздел «Лента заказов»")
    def test_go_to_feed(self, driver):
        page = MainPage(driver)

        page.open_main()
        page.go_to_feed()

        assert page.has_current_url(FEED_URL)

    @allure.title("Переход по клику на «Конструктор»")
    def test_go_to_constructor(self, driver):
        page = MainPage(driver)

        page.open_main()
        page.go_to_feed()
        page.go_to_constructor()

        assert page.has_current_url(BASE_URL)

    @allure.title("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_ingredient_modal_open(self, driver):
        page = MainPage(driver)

        page.open_main()
        page.open_first_bun()

        assert page.is_ingredient_modal_opened()

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_ingredient_modal_close_by_cross(self, driver):
        page = MainPage(driver)

        page.open_main()
        page.open_first_bun()
        page.close_ingredient_modal()

        assert page.is_ingredient_modal_closed()

    @allure.title("При добавлении ингредиента в заказ счётчик увеличивается")
    def test_ingredient_counter_increases(self, driver):
        page = MainPage(driver)

        page.open_main()
        before = page.get_bun_counter()
        page.add_bun_to_constructor()
        page.wait_bun_counter_equals(before + 2)
        after = page.get_bun_counter()

        assert after > before