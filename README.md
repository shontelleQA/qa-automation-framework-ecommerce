# 📦 E-Commerce UI Automation Framework

**A Python + Selenium end-to-end testing framework built for real-world workflows**

This project is my primary SDET portfolio framework — a full UI automation suite that covers functional flows, cross-page interactions, negative paths, and end-to-end checkout logic for a sample e-commerce application.

It's built using Python, Selenium WebDriver, PyTest, and the Page Object Model, with a clean architecture that separates locators, page actions, helpers, and configuration so tests stay readable and scalable.

If you're evaluating my technical work for QA Automation or SDET roles, this is the best place to start.

---

## 📁 Project Goals

This repo is part of my long-term technical portfolio as I transition deeper into SDET + data-aware QA roles.

The goal is to show:

- I understand UI automation at a framework level
- I can structure tests cleanly and sustainably
- I can work across tools (Selenium + Robot + Python automation)
- I think like a QA engineer who cares about correctness, stability, and maintainability
- I write automation that mirrors real user behavior, not toy examples

---

## 🧠 What This Framework Covers

This project replicates the kind of UI automation work you'd find in an actual engineering org:

- **Full Page Object Model (POM)**
- **Reusable components** (e.g., notification bars)
- **Config-driven browser selection** (Chrome, Firefox)
- **Custom Selenium extensions** for waits and interaction stability
- **PyTest fixtures** and a centralized test configuration
- **End-to-end checkout flow** as a realistic SDET scenario
- **Database validation hooks** for order verification
- **Clean test layers** separating setup, actions, assertions, and helpers
- **A contained Robot Framework suite** for alternative automation use

The framework is designed with extensibility in mind and rns locally with minimal setup.

---

## 🏗 Framework Architecture

The framework follows the classic SDET separation of concerns:

### `src/`
Framework engine and supporting code.
```
src/
  pages/          # Page Object classes
  locators/       # All element locators for each page
  helpers/        # Database helpers, API helpers, Selenium extensions
  components/     # Small UI components reused across pages
  configs/        # Config values, generic settings, environment parsing
```

### `tests/`
Human-readable PyTest suites.
```
tests/
  end_to_end/     # Full checkout workflow
  my_account/     # Login, registration, negative tests
  sanity/         # Quick smoke tests
```

### `robot/`
A small, contained Robot Framework suite demonstrating hybrid-framework skills.
```
robot/
  tests/
  resources/
  keywords/
```

---

## 🧪 Highlighted Test: Guest Checkout (End-to-End)

This is the flagship flow in the project. It covers:

- Adding an item to the cart
- Applying a coupon (when valid)
- Filling out billing information
- Placing an order
- Landing on the order confirmation page
- Retrieving the Order ID
- Verifying the order exists in the database

It's written like a real production regression test, combining UI and back-end validation.

---

## 🚀 Running the Tests (Quick Overview)

This framework uses PyTest and supports browser selection through an environment variable.

To run it locally:

- Install dependencies: `pip install -r requirements.txt`
- Set a browser (`BROWSER=chrome` or `BROWSER=firefox`)
- Execute with `pytest`

Robot Framework tests live in the `/robot` folder and run with the `robot` command.

---

## 🔧 Technologies Used

- Python 3.x
- Selenium WebDriver
- PyTest
- Page Object Model (POM)
- MySQL (validation)
- Robot Framework
- SeleniumLibrary (for Robot)
- Environment-based config loading

---

## 🛠 Future Enhancements

Because a good framework evolves over time, planned improvements include:

- CI integration (GitHub Actions)
- Cross-browser test matrix
- Allure reports
- API-level preconditions
- Additional checkout variations
- Expanded Robot tests
- Mocking helpers for test data creation

---

## 📬 Contact

If you're reviewing this for hiring or collaboration, feel free to reach out.  
I'm always open to great engineering conversations.