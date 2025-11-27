# HomePageLocators.py
# -------------------
# Contains locator definitions for elements that live on the Home page.

from selenium.webdriver.common.by import By


class HomePageLocators:
    # Locator for the first "Add to cart" button on the homepage
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "a.add_to_cart_button")
