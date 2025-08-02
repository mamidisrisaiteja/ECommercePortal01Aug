"""
Inventory step definitions for BDD tests
"""
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

# Load scenarios from feature file
scenarios('../features/inventory.feature')

@when('user clicks Sort Icon')
def user_clicks_sort_icon(page, products_page):
    """Click sort dropdown"""
    products_page.click_element(products_page.SORT_DROPDOWN)

@when('user clicks Sort the Products by Name (A–Z)')
def user_sorts_products_a_to_z(page, products_page):
    """Sort products by name A to Z"""
    products_page.sort_products_by_name_a_to_z()

@then('all the products must be sorted from A to Z')
def verify_products_sorted_a_to_z(page, products_page):
    """Verify products are sorted A to Z"""
    assert products_page.verify_products_sorted_a_to_z(), "Products are not sorted from A to Z"

@then(parsers.parse('verify page has text "{text}"'))
def verify_page_has_text_inventory(page, text):
    """Verify page contains specific text"""
    assert text in page.content(), f"Page does not contain text: {text}"
