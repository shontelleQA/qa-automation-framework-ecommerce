*** Settings ***
Library    SeleniumLibrary
Resource   ../resources/variables.resource
Resource   ../resources/locators.resource

*** Keywords ***
Apply Coupon
    ${toggle_present}=    Run Keyword And Return Status    Element Should Be Visible    ${COUPON_TOGGLE}
    IF    ${toggle_present}
        Scroll Page    0    300
        Click Element    ${COUPON_TOGGLE}
    END

    Wait Until Page Contains Element    ${COUPON_FIELD}    timeout=30s
    Wait Until Element Is Visible       ${COUPON_FIELD}    timeout=10s

    Input Text       ${COUPON_FIELD}    ska100
    Click Button     ${APPLY_COUPON_BUTTON}

    Wait Until Page Contains Element    ${CART_PAGE_MESSAGE}    timeout=20s


Proceed To Checkout
    Click Element    ${PROCEED_TO_CHECKOUT_BTN}
