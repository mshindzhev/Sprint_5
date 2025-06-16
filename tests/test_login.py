import data
import helpers
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestLogin:

    def test_login_user(self, driver, main_page):
        driver.find_element(*Locators.BUTTON_OPEN_WINDOW_LOGIN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.INPUT_EMAIL))
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(data.EXISTING_USER_EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(data.PASSWORD)
        driver.find_element(*Locators.BUTTON_LOG_IN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.IMG_AVATAR_USER))
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.BUTTON_CREATE_AD))
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.TXT_NAME_USER))
        assert driver.current_url == "https://qa-desk.stand.praktikum-services.ru/login"

    def test_logout_user(self, driver, main_page):
        driver.find_element(*Locators.BUTTON_OPEN_WINDOW_LOGIN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.INPUT_EMAIL))
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(data.EXISTING_USER_EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(data.PASSWORD)
        driver.find_element(*Locators.BUTTON_LOG_IN).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.IMG_AVATAR_USER))
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(Locators.BUTTON_CREATE_AD))
        driver.find_element(*Locators.BUTTON_LOG_OUT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.BUTTON_OPEN_WINDOW_LOGIN))
        assert WebDriverWait(driver, 5).until(
            expected_conditions.invisibility_of_element_located(Locators.TXT_NAME_USER))
        assert WebDriverWait(driver, 5).until(
            expected_conditions.invisibility_of_element_located(Locators.IMG_AVATAR_USER))
