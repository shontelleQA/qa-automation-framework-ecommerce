*** Settings ***
Library    SeleniumLibrary
Resource   ../resources/variables.resource
Resource   ../resources/locators.resource

*** Keywords ***
Go To Home Page
    Open Browser    ${BASE_URL}    chrome
    Maximize Browser Window

Click First Add To Cart Button
    Click Element    ${ADD_TO_CART_BUTTON}
