import pytest
from selenium import webdriver

@pytest.fixture 
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit

@pytest.fixture 
def open_main_desk():
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

'Что-то'