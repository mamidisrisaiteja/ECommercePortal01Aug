@cart @smoke
Feature: Cart Module
    As a user
    I want to be able to manage my shopping cart
    So that I can review items before checkout

    Background:
        Given user is on Login Page
        When user enters user name as "standard_user" and password as "secret_sauce"
        And user clicks Login Button
        Then verify page has text "Products"

    @TC_CART_01
    Scenario: View cart contents
        And user clicks Add to cart
        And user clicks cart icon
        Then verify page has text "Your Cart"
