# 01-src/02-tests/my_account/test_login_negative.py

import pytest
from src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:
    """
    TCID-12: Login with non-existing user should show correct error message
    """

    @pytest.mark.tcid12
    def test_login_non_existing_user(self):
        # Create the page object and pass in the browser driver
        my_account = MyAccountSignedOut(self.driver)

        # Step 1: Go to My Account page
        my_account.go_to_my_account()

        # Step 2: Enter fake credentials
        my_account.input_login_username("notarealuser@example.com")
        my_account.input_login_password("fakepassword123")

        # Step 3: Click login button
        my_account.click_login_button()

        # Step 4: (Next lesson) verify error message
        # For now we’ll just leave a placeholder
        # my_account.wait_until_error_displayed("Unknown email address")
        pass
