# CheckoutPage.py
# ----------------
# Page object for the Checkout page: handles billing form and placing orders.

from src.helpers.selenium_extended import SeleniumExtended
from src.pages.locators.CheckoutPageLocators import CheckoutPageLocators
from src.helpers.generic_helpers import generate_random_email_and_password


class CheckoutPage(CheckoutPageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)

    # --- Individual field inputs ---

    def input_billing_first_name(self, first_name=None):
        name = first_name if first_name else "AutomationFName"
        self.sl.wait_and_input_text(self.BILLING_FIRST_NAME_FIELD, name)

    def input_billing_last_name(self, last_name=None):
        lname = last_name if last_name else "AutomationLName"
        self.sl.wait_and_input_text(self.BILLING_LAST_NAME_FIELD, lname)

    def input_billing_address_1(self, address=None):
        addr = address if address else "123 Main Street"
        self.sl.wait_and_input_text(self.BILLING_ADDRESS_1_FIELD, addr)

    def input_billing_city(self, city=None):
        city_val = city if city else "Richmond"
        self.sl.wait_and_input_text(self.BILLING_CITY_FIELD, city_val)

    def input_billing_postcode(self, postcode=None):
        zip_val = postcode if postcode else "23220"
        self.sl.wait_and_input_text(self.BILLING_POSTCODE_FIELD, zip_val)

    def input_billing_phone(self, phone=None):
        phone_val = phone if phone else "8045559876"
        self.sl.wait_and_input_text(self.BILLING_PHONE_FIELD, phone_val)

    def input_billing_email(self, email=None):
        if not email:
            email, _ = generate_random_email_and_password()
        self.sl.wait_and_input_text(self.BILLING_EMAIL_FIELD, email)

    # --- Combined helper ---
    def fill_in_billing_info(
        self, f_name=None, l_name=None, street=None, city=None, zip_code=None, phone=None, email=None
    ):
        """Fill out all mandatory billing fields with defaults if none provided."""
        self.input_billing_first_name(f_name)
        self.input_billing_last_name(l_name)
        self.input_billing_address_1(street)
        self.input_billing_city(city)
        self.input_billing_postcode(zip_code)
        self.input_billing_phone(phone)
        self.input_billing_email(email)

    # --- Place order ---
    def click_place_order(self):
        """Click the 'Place order' button, handling intercepted clicks."""
        try:
            self.sl.wait_and_click(self.PLACE_ORDER_BUTTON)
        except Exception:
            # Sometimes another element may block it briefly
            import time
            time.sleep(2)
            self.sl.wait_and_click(self.PLACE_ORDER_BUTTON)
