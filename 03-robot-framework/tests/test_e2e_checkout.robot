*** Settings ***
Documentation     End-to-end checkout test for a guest user
Resource          ../keywords/home_keywords.robot
Resource          ../keywords/header_keywords.robot
Resource          ../keywords/cart_keywords.robot
Resource          ../keywords/checkout_keywords.robot
Resource          ../keywords/order_received_keywords.robot

*** Test Cases ***
E2E Checkout Guest User
    Go To Home Page
    Click First Add To Cart Button
    Click Cart Icon
    Apply Coupon
    Proceed To Checkout
    Fill Billing Info
    Click Place Order
    Verify Order Received Page Loaded
    [Teardown]    Close Browser
