*** Settings ***
Library    SeleniumLibrary
Resource   ../resources/variables.resource
Resource   ../resources/locators.resource

*** Keywords ***
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
    [Arguments]    ${value}=test${random}@email.com
    Input Text    ${BILLING_EMAIL_FIELD}    ${value}

Fill Billing Info
    Wait Until Element Is Visible    ${BILLING_FIRST_NAME_FIELD}    timeout=20s
    Input Billing First Name
    Input Billing Last Name
    Input Billing Address
    Input Billing City
    Input Billing Postcode
    Input Billing Phone
    Input Billing Email


Click Place Order
    Click Button    ${PLACE_ORDER_BUTTON}
