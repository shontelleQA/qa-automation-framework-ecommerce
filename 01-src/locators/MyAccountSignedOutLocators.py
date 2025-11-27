from selenium.webdriver.common.by import By


class MyAccountSignedOutLocators:
    # existing login locators
    LOGIN_USERNAME = (By.ID, "username")
    LOGIN_PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name='login']")
    ERRORS_UL = (By.CSS_SELECTOR, "ul.woocommerce-error")

    # 🆕 registration locators
    REGISTER_EMAIL = (By.ID, "reg_email")
    REGISTER_PASSWORD = (By.ID, "reg_password")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[value='Register']")
