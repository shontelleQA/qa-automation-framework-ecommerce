from src.helpers.selenium_extended import SeleniumExtended
from src.pages.locators.MyAccountSignedInLocators import MyAccountSignedInLocators as L

class MyAccountSignedIn:
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)

    def verify_user_is_signed_in(self):
        """
        Wait for the Logout link in the left nav to become visible.
        If visible, assume the user is logged in.
        """
        self.sl.wait_until_element_is_visible(L.LEFT_NAV_LOGOUT_BTN)
