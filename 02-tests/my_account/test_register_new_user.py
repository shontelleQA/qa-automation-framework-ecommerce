import pytest
from src.pages.MyAccountSignedOut import MyAccountSignedOut
from src.helpers.generic_helpers import generate_random_email_and_password
from src.pages.MyAccountSignedIn import MyAccountSignedIn




@pytest.mark.usefixtures("init_driver")
@pytest.mark.tcid13
class TestRegisterNewUser:

    @pytest.mark.tcid13
    def test_register_valid_new_user(self):
        """
        TCID-13: Verify a new user can register successfully.
        """

        # 1️⃣ Create the page object
        my_account = MyAccountSignedOut(self.driver)

        # 2️⃣ Go to My Account page
        my_account.go_to_my_account()

        # 3️⃣ Fill in registration form (now with random credentials)
        from src.helpers.generic_helpers import generate_random_email_and_password

        rand_info = generate_random_email_and_password()
        email = rand_info["email"]
        password = rand_info["password"]

        print(f"🧪 Using test user: {email} / {password}")

        my_account.input_register_email(email)
        my_account.input_register_password(password)

        # 4️⃣ Click the register button
        my_account.click_register_button()

        # 🧩 Expected Result:
        # After successful registration, the user should be logged in automatically

        # 4️⃣ Verify the user is logged in (My Account page visible)
        my_account_in = MyAccountSignedIn(self.driver)
        my_account_in.verify_user_is_signed_in()

        print("✅ User registration successful and logged in!")
