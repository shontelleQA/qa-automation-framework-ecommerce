# OrderReceivedPage.py
# --------------------
# Page object for the Order Received (confirmation) page.

from src.helpers.selenium_extended import SeleniumExtended
from src.pages.locators.OrderReceivedLocators import OrderReceivedLocators


class OrderReceivedPage(OrderReceivedLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)

    def verify_order_received_page_loaded(self):
        """Wait until the 'Order received' header is visible and contains correct text."""
        expected_text = "Order received"
        self.sl.wait_until_element_contains_text(
            self.ORDER_RECEIVED_HEADER, expected_text
        )
