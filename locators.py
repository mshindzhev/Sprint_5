from selenium.webdriver.common.by import By


class Locators:
    BUTTON_OPEN_WINDOW_LOGIN = By.XPATH, ".//button[text() = 'Вход и регистрация']"
    INPUT_EMAIL = By.NAME, "email"
    INPUT_PASSWORD = By.NAME, "password"

