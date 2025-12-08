*** Settings ***
Documentation     Tests for verifying header navigation links.
Resource          ../keywords/home_keywords.robot
Resource          ../keywords/header_keywords.robot

*** Test Cases ***
Header Navigates To Cart Page
    Go To Home Page
    Click Cart Icon
    Page Should Contain Element    css:.wp-block-woocommerce-cart

Header Navigates To My Account Page
    Go To Home Page
    Click My Account Link
    Page Should Contain    My account
    Page Should Contain Element    id:username
