*** Settings ***
Resource    ../keywords/home_keywords.robot
Resource    ../keywords/header_keywords.robot
Resource    ../keywords/cart_keywords.robot
Resource    ../keywords/checkout_keywords.robot
Resource    ../keywords/order_received_keywords.robot

*** Test Cases ***
Cart Count Updates After Adding Item
    Go To Home Page
    Click First Add To Cart Button
    Verify Cart Count Is    1
    [Teardown]    Close Browser
