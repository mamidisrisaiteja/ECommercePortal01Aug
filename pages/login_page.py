"""
Login Page Object Model
"""
from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
    # Locators
    USERNAME_INPUT = '[data-test="username"]'
    PASSWORD_INPUT = '[data-test="password"]'
    LOGIN_BUTTON = '[data-test="login-button"]'
    ERROR_MESSAGE = '[data-test="error"]'
    LOGO = '.login_logo'
    
    def navigate_to_login_page(self) -> None:
        """Navigate to the login page"""
        self.navigate_to()
        self.wait_for_page_load()
        
    def enter_username(self, username: str) -> None:
        """Enter username in the username field"""
        self.fill_element(self.USERNAME_INPUT, username)
        
    def enter_password(self, password: str) -> None:
        """Enter password in the password field"""
        self.fill_element(self.PASSWORD_INPUT, password)
        
    def click_login_button(self) -> None:
        """Click the login button"""
        self.click_element(self.LOGIN_BUTTON)
        
    def login_with_credentials(self, username: str, password: str) -> None:
        """Complete login process with given credentials"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        
    def login_with_valid_credentials(self) -> None:
        """Login with valid credentials from config"""
        valid_user = self.config['test_users']['valid_user']
        self.login_with_credentials(valid_user['username'], valid_user['password'])
        
    def login_with_invalid_credentials(self) -> None:
        """Login with invalid credentials from config"""
        invalid_user = self.config['test_users']['invalid_user']
        self.login_with_credentials(invalid_user['username'], invalid_user['password'])
        
    def is_login_button_visible(self) -> bool:
        """Check if login button is visible"""
        return self.is_element_visible(self.LOGIN_BUTTON)
        
    def get_error_message(self) -> str:
        """Get error message text"""
        return self.get_text(self.ERROR_MESSAGE)
        
    def is_error_message_displayed(self) -> bool:
        """Check if error message is displayed"""
        return self.is_element_visible(self.ERROR_MESSAGE)
        
    def verify_login_page_loaded(self) -> bool:
        """Verify that login page is loaded"""
        return self.is_element_visible(self.LOGO) and self.is_element_visible(self.LOGIN_BUTTON)
