# HeaderLocators.py
# -----------------
# Contains locator definitions for elements that live in the top navigation header.

from selenium.webdriver.common.by import By


class HeaderLocators:
    # The <ul> element representing the cart icon area in the header
    CART_ICON = (By.ID, "site-header-cart")
