*** Settings ***
Library    SeleniumLibrary
Resource   ../resources/variables.resource
Resource   ../resources/locators.resource

*** Keywords ***
Click Cart Icon
    Click Element    ${CART_ICON}

Click My Account Link
    Click Element    ${MY_ACCOUNT_LINK}

