# conftest.py
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(scope="class")
def init_driver(request):
    """Start a browser for each test class and close it afterward."""

    supported = [
        "chrome", "ch",
        "firefox", "ff",
        "headlesschrome", "headless_chrome",
        "headlessfirefox", "headless_firefox"
    ]

    # 1️⃣ Check for environment variable
    browser = os.environ.get("BROWSER")
    if not browser:
        raise Exception("Environment variable 'BROWSER' must be set (e.g. chrome, firefox).")

    browser = browser.lower()
    if browser not in supported:
        raise Exception(f"'{browser}' not supported. Use one of: {supported}")

    # 2️⃣ Start the correct driver
    if browser in ("chrome", "ch"):
        driver = webdriver.Chrome()

    elif browser in ("firefox", "ff"):
        driver = webdriver.Firefox()

    elif browser in ("headlesschrome", "headless_chrome"):
        opts = ChromeOptions()
        opts.add_argument("--headless=new")
        opts.add_argument("--disable-gpu")
        opts.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=opts)

    elif browser in ("headlessfirefox", "headless_firefox"):
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        opts.add_argument("--disable-gpu")
        opts.add_argument("--no-sandbox")
        driver = webdriver.Firefox(options=opts)

    # 3️⃣ Attach driver to the test class
    request.cls.driver = driver

    # 4️⃣ Yield = hand control to the test
    yield

    # 5️⃣ After the test
    driver.quit()
