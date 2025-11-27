# 🧩 UI Automation Framework — Internal Documentation

This document explains how the core automation framework is built behind the scenes.  
If you're reviewing the code for maintainability, architecture, or implementation details, this is the place to start.

The goal of this framework is simple:  
**make UI tests stable, readable, scalable, and easy to extend as the application grows.**

Everything in the repo is structured around that philosophy.

---

## 🏗 Framework Philosophy

The framework is intentionally designed to behave like a lightweight internal QA tool you'd find in a real engineering org:

- Each page has a dedicated **Page Object**
- All selectors live in **locator files**, not buried in the code
- Cross-page UI widgets (like notification bars) live in **components**
- All "helper logic" (waits, DB checks, API calls) lives **outside the tests**
- Config is **environment-driven**
- Tests **read like stories**, not scripts

This keeps tests clean and avoids brittle spaghetti automation.

---

## 📁 Project Structure (Detailed)
```
src/
  ├── pages/
  ├── locators/
  ├── components/
  ├── helpers/
  ├── configs/
  └── ...
tests/
  ├── end_to_end/
  ├── my_account/
  └── sanity/
```

Below is how each part works.

---

## 📄 Pages (`src/pages`)

Every page is modeled as a **Page Object**, containing:

- actions (click, type, select, submit)
- assertions or state checks
- navigation helpers

Example pattern:
```python
class HomePage(BasePage):
    def click_first_product(self):
        self.click(self.locators.FIRST_PRODUCT)
```

This keeps UI interactions expressive instead of Selenium-heavy.

**Pages never import Selenium directly** — only the BasePage methods.

---

## 🎯 Locators (`src/locators`)

Each page has a dedicated locator file:

- `HomePageLocators.py`
- `ProductPageLocators.py`
- `CheckoutPageLocators.py`
- `OrderReceivedLocators.py`
- ...

This isolates all element selectors so they can be updated centrally without touching the test logic.

Locators follow the Selenium `By` pattern:
```python
from selenium.webdriver.common.by import By

class CheckoutPageLocators:
    BILLING_FIRST_NAME = (By.ID, "billing_first_name")
```

---

## 🧱 Components (`src/components`)

Components are **"micro-POMs"** for reusable UI fragments like:

- Notification bar
- Header
- Login menu
- Cart drawer

They act like mini page objects used inside full pages.

This is a real SDET pattern used in larger codebases to avoid duplication.

---

## 🔧 Helpers (`src/helpers`)

This is the **"engine room"** of the framework.

Helpers include:

### Selenium Extended
A custom wrapper around WebDriver with:
- stable click logic
- waits
- JS interaction fallbacks
- retry mechanisms

This reduces flakiness dramatically.

### Config Helper
Centralizes how the framework selects:
- browsers
- base URLs
- environment presets

### Database Helper
Used in the end-to-end checkout test to validate that the Order ID created in the UI actually exists in the database.

This is a real SDET approach: **UI + DB validation**.

### API Helper
Reserved for hybrid API + UI conditions.

---

## 🧭 Config (`src/configs`)

Stores:
- generic configuration
- environment settings
- optional secrets parsing

Browser selection is environment-variable driven:
```bash
BROWSER=chrome
```

---

## 🧪 Tests (`tests/`)

Tests are organized by type:

### `end_to_end/`
Full workflows that cross multiple pages.  
These mimic production regression suites.

Includes:
- `test_checkout_guest_user.py`

This is your flagship scenario.

### `my_account/`
- Login
- Registration
- Negative scenarios
- State validation

### `sanity/`
Quick smoke tests that assert the basic health of the app.

---

## ⚙️ PyTest Setup

### `conftest.py`
Central location for:
- WebDriver setup/teardown
- fixtures
- browser configuration
- test session hooks

### `pytest.ini`
Controls:
- markers
- log format
- default test discovery
- base settings

---

## 🧵 Running Tests (Developer Flow)

The framework is designed to work with minimal friction:

**Install dependencies**
```bash
pip install -r requirements.txt
```

**Select a browser**
```bash
export BROWSER=chrome   # Mac/Linux
set BROWSER=chrome      # Windows
```

**Run all tests**
```bash
pytest
```

**Run specific suites**
```bash
pytest tests/end_to_end
pytest tests/my_account/test_login_negative.py
```

---

## 🧠 Design Considerations

Key goals during construction:

- Reduce duplication
- Keep tests readable like user stories
- Use helpers to avoid repeating boilerplate
- Avoid brittle sleeps
- Centralize all selectors
- Ensure the test runner is clean and extensible

The structure supports team growth — another engineer could onboard quickly.

---

## 🗂 Future Design Enhancements

Features planned for internal framework growth:

- Allure reporting
- Parallel execution
- Test data builders
- API-backed setup steps
- BrowserStack / Sauce Labs integration
- Extended component library
- More durable locator strategies
- Page flows (higher-level reusable sequences)

---

## 💬 Contribution Notes

If another engineer were to extend the framework:

- Add new locators under `/locators`
- Add a new Page Object under `/pages`
- Use helper functions, not raw Selenium calls
- Keep test logic clean, action-heavy in the POM
- Maintain the separation of components vs pages
- Add tests under the correct test suite folder

This keeps the architecture consistent.