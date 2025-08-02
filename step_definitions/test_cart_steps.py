"""
Cart step definitions for BDD tests
"""
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

# Load scenarios from feature file
scenarios('../features/cart.feature')

@when('user clicks Add to cart')
def user_clicks_add_to_cart(page, products_page):
    """Click add to cart button for first product"""
    products_page.add_first_product_to_cart()

@when('user clicks cart icon')
def user_clicks_cart_icon(page, products_page):
    """Click cart icon"""
    products_page.click_cart_icon()

@then(parsers.parse('verify page has text "{text}"'))
def verify_page_has_text_cart(page, text):
    """Verify page contains specific text"""
    assert text in page.content(), f"Page does not contain text: {text}"
