# Diplom_3 — UI автотесты Stellar Burgers

## Описание проекта

Проект содержит автотесты для веб-приложения **Stellar Burgers**.
Тесты написаны с использованием **Python, Pytest, Selenium** и построены по паттерну **Page Object Model**.

Автотесты проверяют основную функциональность приложения и работу раздела **«Лента заказов»**.

Тестирование выполняется в двух браузерах:

* Google Chrome
* Mozilla Firefox

Для формирования отчётов используется **Allure Report**.

# Структура проекта

Diplom_3
│
├── locators
│   ├── main_page_locators.py
│   └── feed_page_locators.py
│
├── pages
│   ├── base_page.py
│   ├── main_page.py
│   └── feed_page.py
│
├── tests
│   ├── conftest.py
│   ├── test_main_functionality.py
│   └── test_feed.py
│
├── utils
│   ├── api_client.py
│   ├── data.py
│   └── urls.py
│
├── pytest.ini
├── requirements.txt
└── README.md

# Установка зависимостей

Создать виртуальное окружение:

> python -m venv venv

Активировать окружение:
Windows
> venv\Scripts\activate

Установить зависимости:

> pip install -r requirements.txt

# Запуск тестов

## Google Chrome

> pytest -q --browser=chrome --alluredir=allure-results-chrome

## Mozilla Firefox

>pytest -q --browser=firefox --alluredir=allure-results-firefox

# Генерация Allure-отчёта

## Chrome

> allure generate allure-results-chrome -o allure-report-chrome --clean
allure open allure-report-chrome

## Firefox

> allure generate allure-results-firefox -o allure-report-firefox --clean
allure open allure-report-firefox

# Покрытые тестами проверки

## Основная функциональность

Проверено:

* переход по клику на **«Конструктор»**
* переход по клику на **«Лента заказов»**
* открытие модального окна при клике на ингредиент
* закрытие модального окна по крестику
* увеличение счётчика ингредиента при добавлении в заказ
## Раздел «Лента заказов»

Проверено:

* увеличение счётчика **«Выполнено за всё время»**
* увеличение счётчика **«Выполнено за сегодня»**
* появление номера заказа в разделе **«В работе»**
# Используемые технологии

* Python
* Pytest
* Selenium WebDriver
* Allure Report
* Page Object Model (POM)
