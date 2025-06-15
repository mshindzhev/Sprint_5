from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:

    def test_registration_new_user(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

    def test_failed_registration_without_password(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

    def test_failed_registration_existing_user(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")