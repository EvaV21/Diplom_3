import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открыть страницу: {url}")
    def open(self, url: str):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Клик по элементу: {locator}")
    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()

    @allure.step("Клик по видимому элементу: {locator}")
    def click_visible(self, locator):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.click()

    @allure.step("Получить текст элемента: {locator}")
    def text(self, locator) -> str:
        el = self.wait.until(EC.visibility_of_element_located(locator))
        return el.text

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

    @allure.step("Drag&Drop через JS (с DataTransfer): {source_locator} -> {target_locator}")
    def drag_and_drop(self, source_locator, target_locator):

        element_from = self.wait.until(
            EC.visibility_of_element_located(source_locator)
        )

        element_to = self.wait.until(
            EC.presence_of_element_located(target_locator)
        )

        self.driver.execute_script("""
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

        """, element_from, element_to)