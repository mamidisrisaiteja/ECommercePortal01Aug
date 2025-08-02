# Contributing to E-Commerce Portal Test Automation Framework

Thank you for your interest in contributing to this project! This document provides guidelines and information for contributors.

## 🤝 How to Contribute

### Reporting Issues
- Use the [GitHub Issues](https://github.com/mamidisrisaiteja/ECommercePortal01Aug/issues) page
- Search existing issues before creating new ones
- Include detailed information:
  - Steps to reproduce
  - Expected vs actual behavior
  - Environment details (OS, Python version, browser)
  - Screenshots if applicable

### Suggesting Enhancements
- Open an issue with the "enhancement" label
- Provide clear description of the proposed feature
- Explain the use case and benefits
- Consider implementation complexity

## 🛠️ Development Setup

### Prerequisites
- Python 3.9+
- Git
- Node.js (for Playwright)
- VS Code (recommended)

### Local Development
1. **Fork and clone**
   ```bash
   git fork https://github.com/mamidisrisaiteja/ECommercePortal01Aug.git
   git clone https://github.com/YOUR_USERNAME/ECommercePortal01Aug.git
   cd ECommercePortal01Aug
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

4. **Create feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 📝 Coding Standards

### Python Style Guide
- Follow [PEP 8](https://pep8.org/) conventions
- Use meaningful variable and function names
- Add docstrings for classes and functions
- Maximum line length: 127 characters

### Code Structure
```python
"""Module docstring explaining purpose."""

import standard_library
import third_party_library
import local_modules


class PageObject:
    """Class docstring explaining purpose.
    
    Attributes:
        page: Playwright page instance
    """
    
    def __init__(self, page):
        """Initialize page object.
        
        Args:
            page: Playwright page instance
        """
        self.page = page
    
    def perform_action(self) -> bool:
        """Perform specific action on page.
        
        Returns:
            bool: True if action successful, False otherwise
        """
        try:
            # Implementation
            return True
        except Exception as e:
            logger.error(f"Action failed: {e}")
            return False
```

### BDD Guidelines
- Use clear, business-readable language
- Follow Given-When-Then structure
- Keep scenarios focused and independent
- Use appropriate tags (@smoke, @auth, @regression)

```gherkin
Feature: User Authentication
  As a customer
  I want to log into the e-commerce portal
  So that I can access my account

  @auth @smoke
  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter valid username and password
    And I click the login button
    Then I should be redirected to the products page
    And I should see the shopping cart icon
```

### Page Object Model
- Inherit from BasePage for common functionality
- Separate locators from actions
- Use meaningful method names
- Handle errors gracefully

```python
class LoginPage(BasePage):
    """Login page object."""
    
    # Locators
    USERNAME_FIELD = "#user-name"
    PASSWORD_FIELD = "#password"
    LOGIN_BUTTON = "#login-button"
    
    def login_with_credentials(self, username: str, password: str) -> bool:
        """Login with provided credentials."""
        try:
            self.fill_element(self.USERNAME_FIELD, username)
            self.fill_element(self.PASSWORD_FIELD, password)
            self.click_element(self.LOGIN_BUTTON)
            return True
        except Exception as e:
            self.logger.error(f"Login failed: {e}")
            return False
```

## 🧪 Testing Guidelines

### Test Structure
- Write tests for new features
- Ensure existing tests pass
- Include both positive and negative test cases
- Use appropriate test data

### Running Tests
```bash
# Run all tests
pytest -v

# Run specific module
pytest tests/test_authentication.py -v

# Run with coverage
pytest --cov=pages --cov=utilities -v

# Run in headed mode for debugging
pytest --headed -v
```

### Test Data Management
- Use `config.yaml` for configuration
- Store test data in `TestData/` directory
- Avoid hardcoded values in test code
- Use parameterized tests for multiple data sets

## 📊 Pull Request Process

### Before Submitting
1. **Update documentation** if needed
2. **Run all tests** and ensure they pass
3. **Check code formatting**
   ```bash
   black .
   flake8 .
   ```
4. **Update version** if applicable

### PR Requirements
- Clear, descriptive title
- Detailed description of changes
- Link to related issue(s)
- Screenshots for UI changes
- Test results summary

### PR Template
```markdown
## Description
Brief description of changes made.

## Related Issue
Fixes #(issue number)

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] All tests pass
- [ ] New tests added
- [ ] Manual testing completed

## Screenshots
Include screenshots for UI changes.

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Tests added/updated
```

## 🏷️ Commit Message Guidelines

### Format
```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code formatting
- `refactor`: Code restructuring
- `test`: Test additions/modifications
- `ci`: CI/CD changes

### Examples
```bash
feat(auth): add password strength validation

fix(cart): resolve quantity update issue
- Fixed decimal quantity handling
- Added validation for negative values

docs(readme): update installation instructions

test(products): add search functionality tests
```

## 🌟 Recognition

### Contributors
Contributors will be recognized in:
- Repository contributors list
- README acknowledgments
- Release notes for significant contributions

### Code Review Process
1. Automated checks (CI/CD pipeline)
2. Manual code review by maintainers
3. Feedback incorporation
4. Final approval and merge

## 📞 Getting Help

### Resources
- [Project Documentation](README.md)
- [Playwright Documentation](https://playwright.dev/)
- [pytest-bdd Documentation](https://pytest-bdd.readthedocs.io/)

### Communication
- GitHub Issues for bug reports and feature requests
- GitHub Discussions for questions and ideas
- Email maintainers for private concerns

## 🎯 Contribution Areas

### High Priority
- Additional test scenarios
- Cross-browser compatibility improvements
- Performance optimizations
- Documentation enhancements

### Medium Priority
- Visual regression testing
- API testing integration
- Mobile testing support
- Accessibility testing

### Low Priority
- Advanced reporting features
- Test data generators
- Custom fixtures
- Integration examples

Thank you for contributing to making this framework better! 🚀
