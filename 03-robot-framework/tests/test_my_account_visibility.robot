*** Settings ***
Documentation     Verify that the My Account page loads and displays core elements.
Resource          ../keywords/home_keywords.robot
Resource          ../keywords/header_keywords.robot

*** Test Cases ***
My Account Page Loads Correctly
    Go To Home Page
    Click My Account Link
    Wait Until Page Contains Element    css:.woocommerce    timeout=10s
    Page Should Contain                  My account
    Page Should Contain Element          css:form.login
    [Teardown]    Close Browser
