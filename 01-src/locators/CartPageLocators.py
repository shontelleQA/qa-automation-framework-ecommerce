# CartPageLocators.py
# -------------------
# Contains locator definitions for fields and buttons on the Cart page.

from selenium.webdriver.common.by import By

class CartPageLocators:
    # Modern WooCommerce Blocks coupon toggle
    COUPON_TOGGLE = (By.CSS_SELECTOR, "div.wc-block-components-panel__button[role='button']")

    # Coupon input and Apply button
    COUPON_FIELD = (By.CSS_SELECTOR, "input#wc-block-components-totals-coupon__input-coupon")
    APPLY_COUPON_BUTTON = (By.CSS_SELECTOR, "button.wc-block-components-totals-coupon__button")

    # Confirmation message after applying coupon
    CART_PAGE_MESSAGE = (By.CSS_SELECTOR, "div.wc-block-components-notice-banner__content")

    # Button text span for proceeding to checkout (block theme)
    PROCEED_TO_CHECKOUT_BTN = (By.XPATH, "//span[text()='Proceed to Checkout']/..")



