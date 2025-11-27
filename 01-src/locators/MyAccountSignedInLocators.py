from selenium.webdriver.common.by import By

class MyAccountSignedInLocators:
    # This targets the left-nav “Logout” link on the My Account page
    LEFT_NAV_LOGOUT_BTN = (By.CSS_SELECTOR, "li.woocommerce-MyAccount-navigation-link--customer-logout a")
