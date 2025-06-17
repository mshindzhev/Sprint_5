import pytest
from selenium import webdriver

import data


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    driver.get(data.URL_MAIN_PAGE)


