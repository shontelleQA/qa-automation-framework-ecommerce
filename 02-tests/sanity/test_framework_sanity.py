import pytest

@pytest.mark.usefixtures("init_driver")
class TestFrameworkSanity:
    def test_open_site(self):
        self.driver.get("https://example.com")
        print("✅ Framework sanity test passed.")

