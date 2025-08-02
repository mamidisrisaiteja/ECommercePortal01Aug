"""
Authentication step definitions for BDD tests
"""
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

# Load scenarios from feature file
scenarios('../features/authentication.feature')

@given('user is on Login Page')
def user_is_on_login_page(page, login_page):
    """Navigate to login page"""
    login_page.navigate_to_login_page()
    assert login_page.verify_login_page_loaded(), "Login page did not load properly"

@when(parsers.parse('user enters user name as "{username}" and password as "{password}"'))
def user_enters_credentials(page, login_page, username, password):
    """Enter username and password"""
    login_page.enter_username(username)
    login_page.enter_password(password)

@when('user clicks Login Button')
def user_clicks_login_button(page, login_page):
    """Click login button"""
    login_page.click_login_button()

@then(parsers.parse('verify page has text "{text}"'))
def verify_page_has_text(page, text):
    """Verify page contains specific text"""
    assert text in page.content(), f"Page does not contain text: {text}"

@then('Login Button should be still displayed')
def login_button_still_displayed(page, login_page):
    """Verify login button is still visible"""
    assert login_page.is_login_button_visible(), "Login button is not displayed"
