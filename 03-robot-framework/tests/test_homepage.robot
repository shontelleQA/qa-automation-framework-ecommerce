*** Settings ***
Documentation     Basic smoke test to verify homepage loads and add-to-cart button works
Resource          ../keywords/home_keywords.robot

*** Test Cases ***
Homepage Smoke Test
    Go To Home Page
    Click First Add To Cart Button
    [Teardown]    Close Browser
