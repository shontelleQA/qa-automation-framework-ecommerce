*** Settings ***
Library    SeleniumLibrary
Resource   ../resources/variables.resource
Resource   ../resources/locators.resource

*** Keywords ***
Verify Order Received Page Loaded
    Wait Until Element Contains    ${ORDER_RECEIVED_HEADER}    Order received    timeout=15s
