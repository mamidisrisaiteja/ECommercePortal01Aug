"""
Demo script showing how to use the framework with Playwright MCP
"""
import asyncio
import sys
import os

# Add project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
import yaml

def load_config():
    """Load configuration"""
    config_path = os.path.join(project_root, 'config.yaml')
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def demo_login_scenarios():
    """Demonstrate login scenarios without Playwright"""
    print("🎭 Demo: Login Scenarios")
    print("=" * 40)
    
    config = load_config()
    
    # TC_AUTH_01: Valid login
    print("📋 TC_AUTH_01: Login with Valid credentials")
    print("Steps:")
    print("  1. Navigate to Login Page")
    print("  2. Enter username: standard_user")
    print("  3. Enter password: secret_sauce")
    print("  4. Click Login Button")
    print("  5. Verify 'Products' text is displayed")
    print("✅ Expected: Successfully login and see Products page")
    print()
    
    # TC_AUTH_02: Invalid login
    print("📋 TC_AUTH_02: Login with invalid credentials")
    print("Steps:")
    print("  1. Navigate to Login Page")
    print("  2. Enter username: standard_use (invalid)")
    print("  3. Enter password: secret_sauce")
    print("  4. Click Login Button")
    print("  5. Verify 'Login' text is still displayed")
    print("✅ Expected: Login fails and Login button still visible")
    print()

def demo_inventory_scenarios():
    """Demonstrate inventory scenarios"""
    print("🎭 Demo: Inventory Scenarios")
    print("=" * 40)
    
    # TC_INV_01: Product listing
    print("📋 TC_INV_01: Verify product listing")
    print("Steps:")
    print("  1. Login with valid credentials")
    print("  2. Verify 'Products' text is displayed")
    print("  3. Verify 'Add to cart' text is displayed")
    print("✅ Expected: Products page shows inventory with add to cart options")
    print()
    
    # TC_INV_02: Sort products
    print("📋 TC_INV_02: Sort products by Name (A–Z)")
    print("Steps:")
    print("  1. Login with valid credentials")
    print("  2. Click Sort dropdown")
    print("  3. Select 'Name (A–Z)' option")
    print("  4. Verify products are sorted alphabetically")
    print("✅ Expected: Products sorted from A to Z")
    print()

def demo_cart_scenarios():
    """Demonstrate cart scenarios"""
    print("🎭 Demo: Cart Scenarios")
    print("=" * 40)
    
    # TC_CART_01: View cart
    print("📋 TC_CART_01: View cart contents")
    print("Steps:")
    print("  1. Login with valid credentials")
    print("  2. Click 'Add to cart' for any product")
    print("  3. Click cart icon")
    print("  4. Verify 'Your Cart' text is displayed")
    print("✅ Expected: Cart page shows selected items")
    print()

def demo_framework_features():
    """Demonstrate framework features"""
    print("🚀 Framework Features Demo")
    print("=" * 50)
    
    print("📁 Project Structure:")
    print("  ├── pages/                  # Page Object Model")
    print("  │   ├── base_page.py       # Common functionality")
    print("  │   ├── login_page.py      # Login page methods")
    print("  │   ├── products_page.py   # Products page methods")
    print("  │   └── cart_page.py       # Cart page methods")
    print("  ├── features/              # Cucumber Gherkin files")
    print("  │   ├── authentication.feature")
    print("  │   ├── inventory.feature")
    print("  │   └── cart.feature")
    print("  ├── step_definitions/      # BDD step implementations")
    print("  ├── tests/                 # Test runners")
    print("  └── utilities/             # Helper functions")
    print()
    
    print("🏷️  Test Tags:")
    print("  @auth      - Authentication tests")
    print("  @inventory - Inventory/product tests")
    print("  @cart      - Shopping cart tests")
    print("  @smoke     - Critical functionality tests")
    print()
    
    print("🧪 Test Execution Commands:")
    print("  pytest                    # Run all tests")
    print("  pytest -m auth           # Run authentication tests")
    print("  pytest -m inventory      # Run inventory tests")
    print("  pytest -m cart          # Run cart tests")
    print("  pytest -m smoke         # Run smoke tests")
    print("  pytest --html=reports/report.html  # Generate HTML report")
    print()
    
    print("🔧 MCP Integration:")
    print("  - Playwright MCP Server for browser automation")
    print("  - Excel MCP Server for test data management")
    print("  - Agent routing compatible through test tags")
    print()

if __name__ == "__main__":
    print("🎪 E-Commerce Portal Test Framework Demo")
    print("=" * 60)
    print()
    
    demo_framework_features()
    demo_login_scenarios()
    demo_inventory_scenarios() 
    demo_cart_scenarios()
    
    print("🎉 Demo Complete!")
    print("=" * 60)
    print()
    print("💡 To run actual tests with Playwright:")
    print("   pytest tests/test_authentication.py -v")
    print()
    print("💡 To see test data from Excel:")
    print("   Check TestData/TestCaseDocument.xlsx")
    print()
    print("💡 To use with MCP servers:")
    print("   The framework is ready to work with configured MCP servers")
    print("   for automated browser actions and test data management.")
