import time
import data
import helpers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators



class TestRegistration:

    def test_registration_new_user(self, driver, main_page):
        driver.find_element(*Locators.BUTTON_OPEN_WINDOW_LOGIN).click()
        WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(Locators.BUTTON_NO_ACCOUNT))
        driver.find_element(*Locators.BUTTON_NO_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.INPUT_EMAIL))
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(helpers.generation_email())
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(data.PASSWORD)
        driver.find_element(*Locators.INPUT_REPEAT_PASSWORD).send_keys(data.PASSWORD)
        driver.find_element(*Locators.BUTTON_CREATE_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.IMG_AVATAR_USER))
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.BUTTON_CREATE_AD))
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.TXT_NAME_USER))
        assert driver.current_url == "https://qa-desk.stand.praktikum-services.ru/regiatration"


    def test_failed_registration_with_invalid_email_and_without_password(self, driver, main_page):
        driver.find_element(*Locators.BUTTON_OPEN_WINDOW_LOGIN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.BUTTON_NO_ACCOUNT))
        driver.find_element(*Locators.BUTTON_NO_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.INPUT_EMAIL))
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(helpers.generation_invalid_email())
        driver.find_element(*Locators.BUTTON_CREATE_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.TXT_ERROR))
        time.sleep(1220)

        # Проверяем поле Email
        email = driver.find_element(By.ID, "email")
        assert email.value_of_css_property("border") == "1px solid rgb(255, 105, 114)", \
            "Email field should have red border (1px solid #FF6972)"

        # Проверяем поле Пароль
        password = driver.find_element(By.ID, "password")
        assert password.value_of_css_property("border") == "1px solid rgb(255, 105, 114)", \
            "Password field should have red border (1px solid #FF6972)"

        # Проверяем поле Повторите пароль
        confirm_password = driver.find_element(By.ID, "confirm-password")
        assert confirm_password.value_of_css_property("border") == "1px solid rgb(255, 105, 114)"

    def test_failed_registration_existing_user(self, driver, main_page):
        driver.find_element(*Locators.BUTTON_OPEN_WINDOW_LOGIN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.BUTTON_NO_ACCOUNT))
        driver.find_element(*Locators.BUTTON_NO_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.INPUT_EMAIL))
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(data.EXISTING_USER_EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(data.PASSWORD)
        driver.find_element(*Locators.INPUT_REPEAT_PASSWORD).send_keys(data.PASSWORD)
        driver.find_element(*Locators.BUTTON_CREATE_ACCOUNT).click()
        time.sleep(120)