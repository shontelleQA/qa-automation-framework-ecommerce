*** Settings ***
Library    SeleniumLibrary
Resource   ../resources/variables.resource
Resource   ../resources/locators.resource

*** Keywords ***
Apply Coupon
    Click Element    ${COUPON_TOGGLE}
    Wait Until Element Is Visible    ${COUPON_FIELD}    timeout=15s
    Input Text       ${COUPON_FIELD}    ska100
    Click Button     ${APPLY_COUPON_BUTTON}
    Wait Until Element Is Visible    ${CART_PAGE_MESSAGE}    timeout=15s

Proceed To Checkout
    Click Element    ${PROCEED_TO_CHECKOUT_BTN}
