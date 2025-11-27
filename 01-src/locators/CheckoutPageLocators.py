# CheckoutPageLocators.py
# ------------------------
# Contains locator definitions for all billing fields and the 'Place order' button.

from selenium.webdriver.common.by import By


class CheckoutPageLocators:
    # Billing details fields
    BILLING_FIRST_NAME_FIELD = (By.ID, "billing_first_name")
    BILLING_LAST_NAME_FIELD = (By.ID, "billing_last_name")
    BILLING_ADDRESS_1_FIELD = (By.ID, "billing_address_1")
    BILLING_CITY_FIELD = (By.ID, "billing_city")
    BILLING_POSTCODE_FIELD = (By.ID, "billing_postcode")
    BILLING_PHONE_FIELD = (By.ID, "billing_phone")
    BILLING_EMAIL_FIELD = (By.ID, "billing_email")

    # Place Order button
    PLACE_ORDER_BUTTON = (By.ID, "place_order")
