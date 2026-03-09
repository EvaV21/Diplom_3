from selenium.webdriver.common.by import By


class FeedPageLocators:
    FEED_HEADER = (By.XPATH, "//h1[contains(.,'Лента заказов')]")

    TOTAL_ALL_TIME = (By.XPATH, "//p[contains(.,'Выполнено за все время')]/following-sibling::p")
    TOTAL_TODAY = (By.XPATH, "//p[contains(.,'Выполнено за сегодня')]/following-sibling::p")
    
    IN_PROGRESS_NUMBERS = (By.XPATH, "//p[contains(.,'В работе')]/following-sibling::ul//li")