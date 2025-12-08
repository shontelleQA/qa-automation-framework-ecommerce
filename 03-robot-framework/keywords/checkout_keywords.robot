*** Settings ***
Library    SeleniumLibrary
Resource   ../resources/variables.resource
Resource   ../resources/locators.resource
Resource   ./cart_keywords.robot    # Import for Scroll Page keyword

*** Keywords ***
Wait For Checkout Form
    # Wait for Blocks checkout container to load
    Wait Until Element Is Visible    css:.wp-block-woocommerce-checkout    timeout=20s
    # Wait for billing form to be interactive (with retries)
    Wait Until Keyword Succeeds    10x    1s    Element Should Be Visible    ${BILLING_FIRST_NAME_FIELD}

Input Billing First Name
    [Arguments]    ${value}=AutomationFName
    Input Text    ${BILLING_FIRST_NAME_FIELD}    ${value}

Input Billing Last Name
    [Arguments]    ${value}=AutomationLName
    Input Text    ${BILLING_LAST_NAME_FIELD}    ${value}

Input Billing Address
    [Arguments]    ${value}=123 Main Street
    Input Text    ${BILLING_ADDRESS_1_FIELD}    ${value}

Input Billing City
    [Arguments]    ${value}=Richmond
    Input Text    ${BILLING_CITY_FIELD}    ${value}

Input Billing Postcode
    [Arguments]    ${value}=23220
    Input Text    ${BILLING_POSTCODE_FIELD}    ${value}

Input Billing Phone
    [Arguments]    ${value}=8045559876
    Input Text    ${BILLING_PHONE_FIELD}    ${value}

Input Billing Email
    [Arguments]    ${value}=testautomation@email.com
    Input Text    ${BILLING_EMAIL_FIELD}    ${value}

Verify Cart Count Is    [Arguments]    ${expected}
    Wait Until Element Contains    ${CART_COUNT_BADGE}    ${expected}    timeout=10s


Fill Billing Info
    # Wait for checkout form to fully load first
    Wait For Checkout Form

    # Now scroll and fill in the form
    Scroll Page    0    500
    Input Billing First Name
    Input Billing Last Name
    Input Billing Address
    Input Billing City
    Input Billing Postcode
    Input Billing Phone
    Input Billing Email

Click Place Order
    Click Button    ${PLACE_ORDER_BUTTON}