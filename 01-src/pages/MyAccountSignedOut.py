from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators.MyAccountSignedOutLocators import MyAccountSignedOutLocators as L
from src.helpers.selenium_extended import SeleniumExtended
from src.helpers.config_helpers import get_base_url
import logging as logger



class MyAccountSignedOut:
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)

    def go_to_my_account(self):
        base_url = get_base_url()
        endpoint = "/my-account/"
        full_url = base_url + endpoint
        self.driver.get(full_url)

    def input_login_username(self, username):
        self.sl.wait_and_input_text(L.LOGIN_USERNAME, username)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(L.LOGIN_PASSWORD, password)

    def click_login_button(self):
        self.sl.wait_and_click(L.LOGIN_BUTTON)

    # -------------------------------
    # 🧩 Registration section
    # -------------------------------
    def input_register_email(self, email):
        self.sl.wait_and_input_text(L.REGISTER_EMAIL, email)

    def input_register_password(self, password):
        self.sl.wait_and_input_text(L.REGISTER_PASSWORD, password)

    def click_register_button(self):
        self.sl.wait_and_click(L.REGISTER_BUTTON)

    def wait_until_error_is_displayed(self, expected_error):
        """Wait until the expected error message text appears on the page."""
        self.sl.wait_until_element_contains_text(
            L.ERRORS_UL,
            expected_error
        )
