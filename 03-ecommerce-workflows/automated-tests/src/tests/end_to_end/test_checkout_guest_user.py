import pytest
from src.pages.HomePage import HomePage
from src.pages.CartPage import CartPage
from src.pages.CheckoutPage import CheckoutPage
from src.pages.OrderReceivedPage import OrderReceivedPage
from src.pages.Header import Header


@pytest.mark.usefixtures("init_driver")
class TestE2ECheckoutGuestUser:

    @pytest.mark.tcid33
    def test_end_to_end_checkout_guest_user(self):
        """
        TCID-33: End-to-End Checkout (Guest User)
        Covers add to cart, apply coupon, proceed to checkout,
        fill billing info, and place order.
        """

        # --- Page Objects ---
        home = HomePage(self.driver)
        cart = CartPage(self.driver)
        checkout = CheckoutPage(self.driver)
        order_received = OrderReceivedPage(self.driver)
        header = Header(self.driver)

        # --- Step 1: Go to Home page ---
        home.go_to_home_page()

        # --- Step 2: Add product to cart ---
        home.click_first_add_to_cart_button()

        # --- Step 3: Go to Cart page ---
        header.click_cart_icon()

        # --- Step 4: Apply coupon ---
        cart.apply_coupon()

        # --- Step 5: Proceed to Checkout ---
        cart.click_proceed_to_checkout()

        # --- Step 6: Fill billing info and place order ---
        checkout.fill_in_billing_info()
        checkout.click_place_order()

        # --- Step 7: Verify order confirmation page ---
        order_received.verify_order_received_page_loaded()

        # Temporary assertion to mark test completed
        assert True
