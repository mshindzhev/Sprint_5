from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestCreatingAds:

    def creating_ad_unauthorized_user(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

    def creating_ad_authorized_user(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")