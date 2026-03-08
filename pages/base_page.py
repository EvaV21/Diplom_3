import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from utils.data import DEFAULT_TIMEOUT


class BasePage:
    def __init__(self, driver, timeout=DEFAULT_TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открыть страницу: {url}")
    def open(self, url: str):
        self.driver.get(url)

    @allure.step("Найти видимый элемент: {locator}")
    def find_element_with_wait(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Найти все элементы: {locator}")
    def find_elements_with_wait(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Найти все элементы без ожидания: {locator}")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Клик по элементу: {locator}")
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Клик по видимому элементу: {locator}")
    def click_visible(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.click()

    @allure.step("Получить текст элемента: {locator}")
    def text(self, locator) -> str:
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    @allure.step("Элемент виден: {locator}")
    def is_visible(self, locator) -> bool:
        self.wait.until(EC.visibility_of_element_located(locator))
        return True

    @allure.step("Элемент не виден: {locator}")
    def is_not_visible(self, locator) -> bool:
        self.wait.until(EC.invisibility_of_element_located(locator))
        return True

    @allure.step("Подождать URL содержит: {part}")
    def wait_url_contains(self, part: str):
        self.wait.until(EC.url_contains(part))

    @allure.step("Обновить страницу")
    def refresh_page(self):
        self.driver.refresh()

    @allure.step("Drag&Drop через JS: {source_locator} -> {target_locator}")
    def drag_and_drop(self, source_locator, target_locator):
        element_from = self.wait.until(EC.visibility_of_element_located(source_locator))
        element_to = self.wait.until(EC.presence_of_element_located(target_locator))

        self.driver.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];

            const dataTransfer = new DataTransfer();

            function fireEvent(type, elem, dt) {
                const event = new DragEvent(type, {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dt
                });
                elem.dispatchEvent(event);
            }

            fireEvent('dragstart', source, dataTransfer);
            fireEvent('dragenter', target, dataTransfer);
            fireEvent('dragover',  target, dataTransfer);
            fireEvent('drop',      target, dataTransfer);
            fireEvent('dragend',   source, dataTransfer);
            """,
            element_from,
            element_to
        )

    @allure.step("Получить значение счетчика или 0: {locator}")
    def get_counter_value_or_zero(self, locator) -> int:
        elements = self.find_elements(locator)
        if not elements:
            return 0
        text = elements[0].text.strip()
        return int(text) if text else 0

    @allure.step("Дождаться, что текст элемента равен: {value}")
    def wait_text_equals(self, locator, value: str):
        self.wait.until(EC.text_to_be_present_in_element(locator, value))

    @allure.step("Дождаться увеличения числового значения элемента: {locator}")
    def wait_number_increases(self, locator, previous_value: int):
        self.wait.until(
            lambda d: int(self.text(locator)) >= previous_value + 1
        )

    @allure.step("Дождаться появления номера заказа в списке")
    def wait_until(self, condition):
        self.wait.until(condition)

    @allure.step("Проверить, что элемент есть в списке")
    def has_text_in_elements(self, locator, target_text: str) -> bool:
        elements = self.find_elements(locator)
        return any((element.text.strip().lstrip("0") or "0") == target_text for element in elements)

    @allure.step("Безопасно проверить условие ожидания")
    def wait_until_true(self, condition) -> bool:
        try:
            self.wait.until(lambda d: condition())
            return True
        except TimeoutException:
            return False