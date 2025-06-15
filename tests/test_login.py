from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:

    def user_login(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

    def user_logout(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
