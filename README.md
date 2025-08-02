<<<<<<< HEAD
# E-Commerce Portal Test Automation Framework

A Python-based test automation framework using Playwright, Pytest, and Cucumber BDD for testing e-commerce portal functionality.

## Framework Structure

```
ECommercePortal17_01Aug/
├── pages/                    # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py         # Base page with common functionality
│   ├── login_page.py        # Login page objects and methods
│   ├── products_page.py     # Products/Inventory page objects
│   └── cart_page.py         # Shopping cart page objects
├── features/                 # Cucumber Gherkin feature files
│   ├── authentication.feature
│   ├── inventory.feature
│   └── cart.feature
├── step_definitions/         # BDD step definitions
│   ├── __init__.py
│   ├── test_authentication_steps.py
│   ├── test_inventory_steps.py
│   └── test_cart_steps.py
├── tests/                    # Test runners
│   ├── __init__.py
│   ├── test_authentication.py
│   ├── test_inventory.py
│   └── test_cart.py
├── utilities/                # Helper utilities
│   ├── __init__.py
│   └── helpers.py
├── TestData/                 # Test data files
│   └── TestCaseDocument.xlsx
├── config.yaml              # Configuration file
├── conftest.py              # Pytest fixtures and configuration
├── requirements.txt         # Python dependencies
├── pyproject.toml          # Project configuration
└── README.md               # This file
```

## Features

- **Page Object Model**: Modular and maintainable page objects
- **BDD Testing**: Cucumber Gherkin syntax for readable test scenarios
- **Playwright Integration**: Modern browser automation
- **Pytest Framework**: Powerful testing framework with fixtures
- **Tagged Tests**: Organized by modules (@auth, @inventory, @cart, @smoke)
- **Configuration Management**: YAML-based configuration
- **Screenshot on Failure**: Automatic screenshot capture for failed tests
- **HTML Reporting**: Detailed test reports
- **Parallel Execution**: Support for running tests in parallel

## Test Scenarios Covered

### Authentication Module (@auth)
- **TC_AUTH_01**: Login with valid credentials
- **TC_AUTH_02**: Login with invalid credentials

### Inventory Module (@inventory)
- **TC_INV_01**: Verify product listing
- **TC_INV_02**: Sort products by Name (A–Z)

### Cart Module (@cart)
- **TC_CART_01**: View cart contents

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Install Playwright browsers:
```bash
playwright install
```

## Configuration

Update `config.yaml` with your test environment settings:

```yaml
base_url: "https://www.saucedemo.com"
browser: "chromium"  # chromium, firefox, webkit
headless: false
timeout: 30000
```

## Running Tests

### Run all tests:
```bash
pytest
```

### Run tests by module:
```bash
pytest -m auth          # Authentication tests
pytest -m inventory     # Inventory tests  
pytest -m cart          # Cart tests
pytest -m smoke         # Smoke tests
```

### Run specific test scenarios:
```bash
pytest tests/test_authentication.py
pytest tests/test_inventory.py
pytest tests/test_cart.py
```

### Run tests with HTML report:
```bash
pytest --html=reports/report.html --self-contained-html
```

### Run tests in parallel:
```bash
pytest -n auto
```

## Test Data

Test scenarios and data are managed through:
- **Excel File**: `TestData/TestCaseDocument.xlsx` contains test case definitions
- **Config File**: `config.yaml` contains test users and environment settings
- **Feature Files**: Gherkin scenarios in the `features/` directory

## Key Components

### Page Objects
- **BasePage**: Common functionality for all pages
- **LoginPage**: Login page specific methods
- **ProductsPage**: Product listing and sorting functionality
- **CartPage**: Shopping cart operations

### Fixtures (conftest.py)
- **browser_context**: Browser setup and teardown
- **page**: Page instance for tests
- **login_page, products_page, cart_page**: Page object instances

### Step Definitions
- Reusable step definitions for Gherkin scenarios
- Modular organization by feature area
- Natural language interpretation for test actions

## Reporting

- **HTML Reports**: Generated in `reports/` directory
- **Screenshots**: Captured on test failure in `screenshots/` directory
- **Videos**: Optional video recording for failed tests
- **Logs**: Detailed logging with configurable levels

## Best Practices Implemented

1. **Page Object Model**: Separation of page structure from test logic
2. **BDD Approach**: Business-readable test scenarios
3. **Fixture-based Setup**: Reusable test setup and teardown
4. **Configuration Management**: Environment-specific settings
5. **Error Handling**: Robust error handling and reporting
6. **Modular Design**: Organized code structure for maintainability
7. **Tagged Testing**: Organized test execution by categories

## MCP Integration

The framework is designed to work with MCP (Model Context Protocol) servers:
- **Playwright MCP**: Browser automation through MCP
- **Excel MCP**: Test data reading from Excel files
- **Agent Routing**: Compatible with MCP's agent routing logic through test tags

## Contributing

1. Follow the existing code structure and naming conventions
2. Add appropriate test tags for new scenarios
3. Update documentation for new features
4. Ensure all tests pass before submitting changes
=======
# ECommercePortal01Aug
Python Playwright Pytest Cucumber BDD Test Automation Framework for E-Commerce Portal with Page Object Model design pattern, MCP server integration, and comprehensive test scenarios for authentication, inventory, and cart modules.
>>>>>>> 7e0ebf01cec106c97ef808120c59c4e3830d8825
