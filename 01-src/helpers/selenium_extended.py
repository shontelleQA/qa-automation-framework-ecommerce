# selenium_extended.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging as logger
import time


class SeleniumExtended:
    """
    A helper class that gives us reusable Selenium actions
    so we don't have to repeat code in every test.
    """

    def __init__(self, driver, default_timeout=10):
        self.driver = driver
        self.default_timeout = default_timeout

    def wait_and_input_text(self, locator, text, timeout=None):
        """
        Wait for an element to appear, then type text into it.
        Example:
            self.sl.wait_and_input_text(L.USERNAME_FIELD, "myname")
        """
        timeout = timeout if timeout else self.default_timeout
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        """
        Wait for an element to be clickable, scroll it into view, and click.
        """
        timeout = timeout if timeout else self.default_timeout
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

        # Scroll into view before clicking (fixes intercepted click)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)

        logger.debug(f"Clicking element: {locator}")
        element.click()

    def wait_until_element_contains_text(self, locator, text, timeout=None):
        """
        Wait until the given element contains the expected text.
        """
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    def wait_until_element_is_visible(self, locator, timeout=None):
        """
        Wait until the element located by 'locator' is visible on the page.
        """
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_and_get_text(self, locator, timeout=10):
        """
        Wait until the element located by 'locator' is visible,
        then return its text content.
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element.text
