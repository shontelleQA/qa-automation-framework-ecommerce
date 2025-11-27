from src.helpers.config_helpers import get_base_url
from src.pages.locators.HomePageLocators import HomePageLocators
from src.helpers.selenium_extended import SeleniumExtended


class HomePage(HomePageLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)

    def go_to_home_page(self):
        base_url = get_base_url()
        self.driver.get(base_url)

    def click_first_add_to_cart_button(self):
        self.sl.wait_and_click(self.ADD_TO_CART_BUTTON)
