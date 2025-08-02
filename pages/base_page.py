"""
Base Page class containing common functionality for all page objects
"""
from playwright.sync_api import Page, Locator
from typing import Optional
import yaml
import os

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.config = self._load_config()
        
    def _load_config(self) -> dict:
        """Load configuration from config.yaml"""
        config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.yaml')
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
    
    def navigate_to(self, url: str = None) -> None:
        """Navigate to a specific URL or base URL if no URL provided"""
        if url is None:
            url = self.config['base_url']
        self.page.goto(url)
        
    def wait_for_element(self, selector: str, timeout: Optional[int] = None) -> Locator:
        """Wait for element to be visible"""
        if timeout is None:
            timeout = self.config.get('timeout', 30000)
        return self.page.wait_for_selector(selector, timeout=timeout)
        
    def click_element(self, selector: str) -> None:
        """Click on an element"""
        element = self.wait_for_element(selector)
        element.click()
        
    def fill_element(self, selector: str, text: str) -> None:
        """Fill text in an element"""
        element = self.wait_for_element(selector)
        element.fill(text)
        
    def get_text(self, selector: str) -> str:
        """Get text from an element"""
        element = self.wait_for_element(selector)
        return element.text_content()
        
    def is_element_visible(self, selector: str, timeout: Optional[int] = None) -> bool:
        """Check if element is visible"""
        try:
            if timeout is None:
                timeout = self.config.get('wait_time', 5) * 1000
            self.page.wait_for_selector(selector, timeout=timeout)
            return True
        except:
            return False
            
    def verify_page_contains_text(self, text: str) -> bool:
        """Verify if page contains specific text"""
        return text in self.page.content()
        
    def take_screenshot(self, name: str) -> None:
        """Take a screenshot"""
        screenshots_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'screenshots')
        os.makedirs(screenshots_dir, exist_ok=True)
        self.page.screenshot(path=f"{screenshots_dir}/{name}.png")
        
    def get_page_title(self) -> str:
        """Get page title"""
        return self.page.title()
        
    def wait_for_page_load(self) -> None:
        """Wait for page to load completely"""
        self.page.wait_for_load_state('networkidle')
