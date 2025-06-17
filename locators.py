from selenium.webdriver.common.by import By


class Locators:

    # for registration_and_login
    BUTTON_OPEN_WINDOW_LOGIN = By.XPATH, ".//button[text() = 'Вход и регистрация']"
    INPUT_EMAIL = By.NAME, "email"
    INPUT_PASSWORD = By.NAME, "password"
    INPUT_REPEAT_PASSWORD = By.NAME, "submitPassword"
    BUTTON_NO_ACCOUNT = By.XPATH, ".//button[text() = 'Нет аккаунта']"
    BUTTON_CREATE_ACCOUNT = By.XPATH, ".//button[text() = 'Создать аккаунт']"
    IMG_AVATAR_USER = By.CLASS_NAME, "svgSmall"
    TXT_NAME_USER = By.XPATH, ".//h3[text()='User.']"
    BUTTON_CREATE_AD = By.XPATH, ".//button[text() = 'Разместить объявление']"
    TXT_ERROR = By.XPATH, ".//span[text()='Ошибка']"
    FRAME_FIELD_EMAIL = By.XPATH, ".//input[@name='email']/ancestor::div[@class='input_inputError__fLUP9']"
    FRAME_FIELD_PASSWORD = By.XPATH, ".//input[@name='password']/ancestor::div[@class='input_inputError__fLUP9']"
    FRAME_FIELD_REPEAT_PASSWORD = By.XPATH, ".//input[@name='submitPassword']/ancestor::div[@class='input_inputError__fLUP9']"
    BUTTON_LOG_IN = By.XPATH, ".//button[text() = 'Войти']"
    BUTTON_LOG_OUT = By.XPATH, ".//button[text() = 'Выйти']"
    TXT_NEED_AUTHORIZATION = By.XPATH, ".//h1[text()='Чтобы разместить объявление, авторизуйтесь']"
    INPUT_NAME_PRODUCT = By.NAME, "name"
    INPUT_DESCRIPTION_PRODUCT = By.XPATH, ".//textarea[@name='description']"
    INPUT_PRICE_PRODUCT = By.NAME, "price"
    RADIO_BUTTON_USED_PRODUCT = By.XPATH, ".//div[@class='radioUnput_inputRegular__FbVbr']"
    BUTTON_PUBLISH_AD = By.XPATH, ".//button[text() = 'Опубликовать']"
    DROPDOWN_CATEGORY = By.XPATH, ".//input[@name='category']/following-sibling::button"
    DROPDOWN_CITY = By.XPATH, ".//input[@name='city']/following-sibling::button"
    POINT_IN_DROPDOWN_CATEGORY = By.XPATH, ".//span[text()='Хобби']"
    POINT_IN_DROPDOWN_CITY = By.XPATH, ".//span[text()='Казань']"

    # for creating_ads





