# OrderReceivedLocators.py
# ------------------------
# Contains locator definitions for the Order Received (confirmation) page.

from selenium.webdriver.common.by import By


class OrderReceivedLocators:
    # The confirmation header that appears after placing an order
    ORDER_RECEIVED_HEADER = (By.CSS_SELECTOR, "h1.entry-title")
