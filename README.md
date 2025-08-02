# ECommercePortal01Aug

Python Playwright Pytest Cucumber BDD Test Automation Framework for E-Commerce Portal with Page Object Model design pattern, MCP server integration, and comprehensive test scenarios for authentication, inventory, and cart modules.

## Recent Updates ✅
- **Fixed BDD test scenario loading issues** - Test files now properly load scenarios from feature files
- **Added basic framework validation tests** - Basic smoke tests to verify framework setup
- **Configured proper pytest-bdd integration** - All test modules now correctly import and use scenarios
- **Enhanced CI/CD pipeline** - Better debugging and error reporting

## Project Structure
- `tests/` - BDD test files that load scenarios from feature files
- `step_definitions/` - Step definition implementations for BDD scenarios
- `features/` - Gherkin feature files with test scenarios
- `pages/` - Page Object Model classes for UI interactions
- `conftest.py` - Pytest configuration and fixtures
- `test_basic.py` - Basic framework validation tests

## Test Modules
- **Authentication Tests** (`tests/test_authentication.py`) - Login and authentication scenarios
- **Cart Tests** (`tests/test_cart.py`) - Shopping cart functionality
- **Inventory Tests** (`tests/test_inventory.py`) - Product browsing and inventory
- **Basic Tests** (`test_basic.py`) - Framework validation and smoke tests

## Running Tests
```bash
# Run all tests
pytest

# Run basic framework tests
pytest test_basic.py

# Run specific test module
pytest tests/test_authentication.py

# Run with verbose output
pytest -v --tb=long
```

## CI/CD Pipeline Status
The GitHub Actions workflow automatically runs tests on every push and pull request. Recent fixes have resolved the scenario loading issues that were preventing tests from being discovered properly.

## Framework Features
- **Page Object Model** design pattern for maintainable code
- **BDD/Gherkin** scenarios for readable test cases
- **Playwright** for modern browser automation
- **pytest-bdd** integration for seamless BDD testing
- **Headless/headed** mode support for CI and debugging
- **Screenshot capture** on test failures
- **HTML reporting** with detailed test results

## Configuration
Tests are configured through `conftest.py` with browser fixtures and page object setup. The framework supports both headless (CI) and headed (local development) execution modes.

**Pipeline Status**: Recently updated with scenario loading fixes - tests should now discover and execute properly! 🚀