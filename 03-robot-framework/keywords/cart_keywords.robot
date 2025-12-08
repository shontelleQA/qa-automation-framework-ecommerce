*** Settings ***
Library    SeleniumLibrary
Resource   ../resources/variables.resource
Resource   ../resources/locators.resource

*** Keywords ***
Scroll Page
    [Arguments]    ${x}=0    ${y}=300
    Execute JavaScript    window.scrollBy(${x}, ${y});

Apply Coupon
    # Try Blocks version first
    ${blocks_toggle_present}=    Run Keyword And Return Status    Element Should Be Visible    ${COUPON_TOGGLE}
    IF    ${blocks_toggle_present}
        Scroll Page    0    300
        Click Element    ${COUPON_TOGGLE}
        Wait Until Page Contains Element    ${COUPON_FIELD}    timeout=20s
        Input Text       ${COUPON_FIELD}    ska100
        Click Button     ${APPLY_COUPON_BUTTON}
        Wait Until Page Contains Element    ${CART_PAGE_MESSAGE}    timeout=20s
        RETURN
    END

    # Classic WooCommerce coupon UI fallback
    Scroll Page    0    300
    Wait Until Page Contains Element    ${CLASSIC_COUPON_FIELD}    timeout=20s
    Input Text    ${CLASSIC_COUPON_FIELD}    ska100
    Click Button    ${CLASSIC_APPLY_COUPON}
    Wait Until Page Contains Element    ${CART_PAGE_MESSAGE}    timeout=20s

Proceed To Checkout
    Click Element    ${PROCEED_TO_CHECKOUT_BTN}
