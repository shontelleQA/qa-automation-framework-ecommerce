*** Settings ***
Library    SeleniumLibrary
Resource   ../resources/variables.resource
Resource   ../resources/locators.resource

*** Keywords ***
Scroll Page
    [Arguments]    ${x}=0    ${y}=300
    Execute JavaScript    window.scrollBy(${x}, ${y});

Apply Coupon
    # Ensure the Blocks cart is loaded
    Wait Until Element Is Visible    css:.wp-block-woocommerce-cart    timeout=10s

    # Give the page time to fully render all interactive elements
    Sleep    2s

    # Scroll to where the coupon area should be
    Scroll Page    0    300
    Sleep    0.5s

    # Try Blocks version first (with longer timeout)
    ${blocks_toggle_present}=    Run Keyword And Return Status
    ...    Wait Until Element Is Visible    ${COUPON_TOGGLE}    timeout=10s

    IF    ${blocks_toggle_present}
        Click Element    ${COUPON_TOGGLE}

        # Wait for dynamic coupon form to appear
        Wait Until Keyword Succeeds    10x    1s    Element Should Be Visible    ${COUPON_FIELD}

        Input Text       ${COUPON_FIELD}    ska100
        Click Element    ${APPLY_COUPON_BUTTON}

        # Wait for snackbar message to appear
        Wait Until Keyword Succeeds    10x    1s    Element Should Be Visible    ${CART_PAGE_MESSAGE}
        RETURN
    END

    # Classic fallback (won't be used, but safe to keep)
    Wait Until Element Is Visible    ${CLASSIC_COUPON_FIELD}    timeout=20s
    Input Text    ${CLASSIC_COUPON_FIELD}    ska100
    Click Button    ${CLASSIC_APPLY_COUPON}
    Wait Until Page Contains Element    css:.woocommerce-message    timeout=20s

Proceed To Checkout
    Click Element    ${PROCEED_TO_CHECKOUT_BTN}
