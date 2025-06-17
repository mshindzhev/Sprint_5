import data
import helpers
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from selenium.webdriver.common.by import By


class TestCreatingAds:

    def test_creating_ad_unauthorized_user(self, driver, main_page):
        driver.find_element(*Locators.BUTTON_CREATE_AD).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.TXT_NEED_AUTHORIZATION))
        assert driver.find_element(*Locators.TXT_NEED_AUTHORIZATION)

    def test_creating_ad_authorized_user(self, driver, main_page):
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
        driver.find_element(*Locators.BUTTON_CREATE_AD).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.INPUT_NAME_PRODUCT))
        name_product = helpers.generation_name_product()
        driver.find_element(*Locators.INPUT_NAME_PRODUCT).send_keys(name_product)
        driver.find_element(*Locators.DROPDOWN_CATEGORY).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.POINT_IN_DROPDOWN_CATEGORY))
        driver.find_element(*Locators.POINT_IN_DROPDOWN_CATEGORY).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.RADIO_BUTTON_USED_PRODUCT))
        driver.find_element(*Locators.RADIO_BUTTON_USED_PRODUCT).click()
        driver.find_element(*Locators.DROPDOWN_CITY).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.POINT_IN_DROPDOWN_CITY))
        driver.find_element(*Locators.POINT_IN_DROPDOWN_CITY).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.INPUT_DESCRIPTION_PRODUCT))
        driver.find_element(*Locators.INPUT_DESCRIPTION_PRODUCT).send_keys(data.DESCRIPTION_PRODUCT)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.INPUT_PRICE_PRODUCT))
        driver.find_element(*Locators.INPUT_PRICE_PRODUCT).send_keys(data.PRICE)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.BUTTON_PUBLISH_AD))
        driver.find_element(*Locators.BUTTON_PUBLISH_AD).click()
        driver.get("https://qa-desk.stand.praktikum-services.ru/profile")
        assert WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, f'.//h2[text()="{name_product}"]')  # Добавлены кавычки
            )
        )


