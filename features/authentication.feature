@auth @smoke
Feature: Authentication Module
    As a user
    I want to be able to login to the e-commerce portal
    So that I can access the application features

    Background:
        Given user is on Login Page

    @TC_AUTH_01
    Scenario: Login with valid credentials
        When user enters user name as "standard_user" and password as "secret_sauce"
        And user clicks Login Button
        Then verify page has text "Products"

    @TC_AUTH_02
    Scenario: Login with invalid credentials
        When user enters user name as "standard_use" and password as "secret_sauce"
        And user clicks Login Button
        Then verify page has text "Login"
        And Login Button should be still displayed
