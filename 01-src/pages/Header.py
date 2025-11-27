# Header.py
# ----------
# Page object for the persistent header/navigation bar.
# Provides actions that can be used across multiple pages (e.g., clicking the cart icon).

from src.helpers.selenium_extended import SeleniumExtended
from src.pages.locators.HeaderLocators import HeaderLocators




class Header(HeaderLocators):
    def __init__(self, driver):
        self.driver = driver
        # Initialize our Selenium helper for wait-and-click style actions
        self.sl = SeleniumExtended(driver)

    def click_cart_icon(self):
        """Click the shopping cart icon in the header."""
        self.sl.wait_and_click(self.CART_ICON)
