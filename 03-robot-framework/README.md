# 📘 Robot Framework Suite

This folder contains a small but realistic set of Robot Framework smoke tests.  
Each test validates a core area of the e-commerce site:

- **Homepage**
- **Header navigation**
- **Cart functionality**
- **My Account page**
- **(Quarantined) E2E checkout test**

The test suite uses:

- **SeleniumLibrary**
- **Shared locators** defined in `resources/locators.resource`
- **Shared variables** from `variables.resource`
- **Reusable keywords** from the `keywords/` directory
