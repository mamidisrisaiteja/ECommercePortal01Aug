"""
Pytest configuration and fixtures for the test framework
"""
import pytest
import yaml
import os
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

def load_config():
    """Load configuration from config.yaml"""
    config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

@pytest.fixture(scope="session")
def config():
    """Provide configuration data"""
    return load_config()

@pytest.fixture(scope="function")
def browser_context(config):
    """Create browser context with Playwright"""
    with sync_playwright() as p:
        browser_type = getattr(p, config.get('browser', 'chromium'))
        browser = browser_type.launch(
            headless=config.get('headless', False),
            slow_mo=500  # Add delay for demo purposes
        )
        context = browser.new_context(
            viewport={'width': 1280, 'height': 720},
            record_video_dir='videos/' if config.get('video_on_failure', False) else None
        )
        yield context
        context.close()
        browser.close()

@pytest.fixture(scope="function")
def page(browser_context):
    """Create a new page"""
    page = browser_context.new_page()
    yield page
    page.close()

@pytest.fixture(scope="function")
def login_page(page):
    """Create LoginPage instance"""
    return LoginPage(page)

@pytest.fixture(scope="function")
def products_page(page):
    """Create ProductsPage instance"""
    return ProductsPage(page)

@pytest.fixture(scope="function")
def cart_page(page):
    """Create CartPage instance"""
    return CartPage(page)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test results and take screenshots on failure"""
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        # Take screenshot on failure
        try:
            page = item.funcargs.get('page')
            if page:
                screenshots_dir = 'screenshots'
                os.makedirs(screenshots_dir, exist_ok=True)
                screenshot_path = f"{screenshots_dir}/failure_{item.name}_{call.when}.png"
                page.screenshot(path=screenshot_path)
                print(f"Screenshot saved: {screenshot_path}")
        except Exception as e:
            print(f"Failed to take screenshot: {e}")

def pytest_configure(config):
    """Configure pytest with custom markers"""
    config.addinivalue_line("markers", "auth: Authentication related tests")
    config.addinivalue_line("markers", "inventory: Inventory related tests")
    config.addinivalue_line("markers", "cart: Cart related tests")
    config.addinivalue_line("markers", "smoke: Smoke tests")

def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers based on test names"""
    for item in items:
        if "auth" in item.name.lower():
            item.add_marker(pytest.mark.auth)
        if "inventory" in item.name.lower() or "inv" in item.name.lower():
            item.add_marker(pytest.mark.inventory)
        if "cart" in item.name.lower():
            item.add_marker(pytest.mark.cart)
        if any(marker in item.name.lower() for marker in ["tc_auth_01", "tc_auth_02", "tc_inv_01", "tc_cart_01"]):
            item.add_marker(pytest.mark.smoke)
