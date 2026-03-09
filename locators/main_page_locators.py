from selenium.webdriver.common.by import By


class MainPageLocators:

    CONSTRUCTOR_TAB = (By.XPATH, "//p[text()='Конструктор']/parent::a")
    FEED_TAB = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")

    FIRST_BUN = (By.XPATH, "//h2[text()='Булки']/following::a[1]")
    FIRST_BUN_COUNTER = (By.XPATH, "//h2[text()='Булки']/following::a[1]//p[contains(@class,'counter')]")

    MODAL = (By.XPATH, "//section[contains(@class,'Modal_modal') and .//h2[contains(.,'Детали ингредиента')]]")
    MODAL_TITLE = (By.XPATH, "//section[contains(@class,'Modal_modal')]//h2[contains(.,'Детали ингредиента')]")
    MODAL_CLOSE = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal') and contains(@class,'Modal_modal_opened')]"
        "//button[contains(@class,'Modal_modal__close')]"
    )

    CONSTRUCTOR_DROP_ZONE = (By.XPATH, "//section[contains(@class,'BurgerConstructor_basket')]")