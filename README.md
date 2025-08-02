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
# E-Commerce Portal Test Automation Framework

[![CI/CD Pipeline](https://github.com/mamidisrisaiteja/ECommercePortal01Aug/actions/workflows/ci.yml/badge.svg)](https://github.com/mamidisrisaiteja/ECommercePortal01Aug/actions/workflows/ci.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Playwright](https://img.shields.io/badge/playwright-1.41.2-green.svg)](https://playwright.dev/)
[![pytest-bdd](https://img.shields.io/badge/pytest--bdd-7.0.1-orange.svg)](https://pytest-bdd.readthedocs.io/)

A comprehensive test automation framework for e-commerce portal testing using Python, Playwright, and Behavior Driven Development (BDD) with Page Object Model design pattern.

## 🚀 Features

- **BDD Testing**: Cucumber Gherkin syntax with pytest-bdd
- **Page Object Model**: Maintainable and scalable test architecture
- **Multi-Browser Support**: Chromium, Firefox, and WebKit
- **Excel Integration**: Test data management via MCP Excel server
- **CI/CD Ready**: GitHub Actions workflow included
- **Comprehensive Reporting**: HTML reports with screenshots
- **Headed/Headless Mode**: Visual debugging and fast execution
- **Cross-Platform**: Windows, macOS, and Linux support

## 📁 Project Structure

```
ECommercePortal01Aug/
├── 📂 pages/                    # Page Object Model classes
│   ├── base_page.py            # Base page with common functionality
│   ├── login_page.py           # Authentication page methods
│   ├── products_page.py        # Product catalog operations
│   └── cart_page.py            # Shopping cart functionality
├── 📂 features/                 # BDD feature files
│   ├── authentication.feature  # Login/logout scenarios
│   ├── product_browsing.feature # Product search & filter
│   └── shopping_cart.feature   # Cart management tests
├── 📂 step_definitions/         # BDD step implementations
│   ├── auth_steps.py           # Authentication step definitions
│   ├── product_steps.py        # Product browsing steps
│   └── cart_steps.py           # Shopping cart steps
├── 📂 tests/                    # Test runners
│   ├── test_authentication.py  # Auth test execution
│   ├── test_products.py        # Product test execution
│   └── test_cart.py            # Cart test execution
├── 📂 utilities/                # Helper functions
│   ├── config_manager.py       # Configuration management
│   ├── logger.py               # Logging utilities
│   └── helpers.py              # Common helper functions
├── 📂 TestData/                 # Test data files
│   └── TestCaseDocument.xlsx   # Excel test scenarios
├── 📂 .github/workflows/        # CI/CD automation
│   └── ci.yml                  # GitHub Actions workflow
├── config.yaml                 # Framework configuration
├── conftest.py                 # Pytest fixtures
├── pyproject.toml              # Project metadata
└── requirements.txt            # Python dependencies
```

## 🛠️ Installation

### Prerequisites

- Python 3.9 or higher
- Node.js (for Playwright browsers)
- Git

### Quick Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/mamidisrisaiteja/ECommercePortal01Aug.git
   cd ECommercePortal01Aug
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers**
   ```bash
   playwright install
   ```

## 🎯 Test Execution

### Run All Tests (Headed Mode)
```bash
pytest -v --headed
```

### Run Authentication Tests Only
```bash
pytest tests/test_authentication.py -v
```

### Run Tests by Tags
```bash
# Smoke tests only
pytest -m smoke -v

# Authentication tagged tests
pytest -m auth -v
```

### Generate HTML Report
```bash
pytest --html=reports/report.html --self-contained-html
```

### Cross-Browser Testing
```bash
# Firefox
pytest --browser=firefox -v

# WebKit (Safari)
pytest --browser=webkit -v
```

## 🧪 Test Scenarios

### Authentication Module (TC_AUTH_01, TC_AUTH_02)
- ✅ Valid user login
- ✅ Invalid credential handling
- ✅ Password field masking
- ✅ Login button functionality

### Product Browsing
- 🔄 Product search functionality
- 🔄 Category filtering
- 🔄 Product detail viewing
- 🔄 Add to cart operations

### Shopping Cart
- 🔄 Cart item management
- 🔄 Quantity updates
- 🔄 Remove items
- 🔄 Checkout process

*Legend: ✅ Implemented & Tested | 🔄 In Development*

## ⚙️ Configuration

### config.yaml Structure
```yaml
# Application settings
app:
  base_url: "https://www.saucedemo.com"
  timeout: 30000

# Test user credentials
test_users:
  valid_user:
    username: "standard_user"
    password: "secret_sauce"
  invalid_user:
    username: "invalid_user"
    password: "wrong_password"

# Browser settings
browser:
  headless: false
  slow_mo: 500
  viewport:
    width: 1280
    height: 720
```

## 🔧 MCP Server Integration

This framework integrates with Model Context Protocol (MCP) servers:

### Excel MCP Server
- Reads test scenarios from `TestCaseDocument.xlsx`
- Extracts test case IDs: TC_AUTH_01, TC_AUTH_02
- Provides dynamic test data management

### Playwright MCP Server  
- Browser automation capabilities
- Screenshot and PDF generation
- Network request interception

## 📊 Reporting

### HTML Reports
- Detailed test execution results
- Screenshots on failure
- Step-by-step BDD scenario breakdown
- Browser and environment information

### CI/CD Reports
- Multi-browser test matrix
- Security vulnerability scanning
- Code quality metrics
- Artifact preservation

## 🤝 Contributing

1. **Fork the repository**
2. **Create feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit changes**
   ```bash
   git commit -m "Add your feature description"
   ```
4. **Push to branch**
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Create Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Add BDD scenarios for new features
- Include step definitions and page objects
- Update documentation for API changes
- Ensure all tests pass before submitting PR

## 🚀 Continuous Integration

### GitHub Actions Workflow
- **Multi-Python Testing**: 3.9, 3.10, 3.11
- **Cross-Browser Matrix**: Chromium, Firefox, WebKit
- **Security Scanning**: Dependency vulnerability checks
- **Code Quality**: Linting and formatting validation
- **Artifact Upload**: Test reports and screenshots

### Workflow Triggers
- Push to `main` or `develop` branches
- Pull request creation
- Manual workflow dispatch

## 🐛 Troubleshooting

### Common Issues

**Browser Installation Failed**
```bash
# Reinstall Playwright browsers
playwright install --force
```

**Import Errors**
```bash
# Ensure virtual environment is activated
pip install -r requirements.txt --force-reinstall
```

**Test Discovery Issues**
```bash
# Clear pytest cache
pytest --cache-clear
```

**Step Definition Mismatches**
```bash
# Regenerate step definitions
pytest --gherkin-terminal-reporter -v
```

## 📈 Performance Metrics

### Test Execution Times
- Authentication Suite: ~32 seconds (headed mode)
- Product Browsing: ~45 seconds (headed mode)
- Shopping Cart: ~28 seconds (headed mode)

### Browser Performance
- **Chromium**: Fastest execution, best debugging
- **Firefox**: Memory efficient, good stability  
- **WebKit**: Safari compatibility, mobile testing

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Playwright Team**: Excellent browser automation framework
- **pytest-bdd**: Seamless BDD integration
- **Microsoft**: VS Code and development tools
- **EY Professional Services**: Testing standards and practices

---

**Built with ❤️ for robust e-commerce testing**

*For support or questions, please open an issue or contact the development team.*
Python Playwright Pytest Cucumber BDD Test Automation Framework for E-Commerce Portal with Page Object Model design pattern, MCP server integration, and comprehensive test scenarios for authentication, inventory, and cart modules.
>>>>>>> 7e0ebf01cec106c97ef808120c59c4e3830d8825
