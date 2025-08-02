"""
Cart Page Object Model
"""
from playwright.sync_api import Page
from pages.base_page import BasePage
from typing import List

class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
    # Locators
    CART_TITLE = '.title'
    CART_ITEMS = '.cart_item'
    CART_ITEM_NAMES = '.inventory_item_name'
    REMOVE_BUTTONS = '[data-test^="remove"]'
    CONTINUE_SHOPPING_BUTTON = '[data-test="continue-shopping"]'
    CHECKOUT_BUTTON = '[data-test="checkout"]'
    CART_QUANTITY = '.cart_quantity'
    
    def verify_cart_page_loaded(self) -> bool:
        """Verify that cart page is loaded"""
        return self.is_element_visible(self.CART_TITLE) and "Your Cart" in self.get_text(self.CART_TITLE)
        
    def verify_your_cart_text_displayed(self) -> bool:
        """Verify 'Your Cart' text is displayed"""
        return self.verify_page_contains_text("Your Cart")
        
    def get_cart_items_count(self) -> int:
        """Get the number of items in cart"""
        return len(self.page.query_selector_all(self.CART_ITEMS))
        
    def get_cart_item_names(self) -> List[str]:
        """Get list of all cart item names"""
        item_elements = self.page.query_selector_all(self.CART_ITEM_NAMES)
        return [element.text_content() for element in item_elements]
        
    def remove_item_from_cart(self, item_name: str) -> None:
        """Remove a specific item from cart by name"""
        remove_button = f'[data-test="remove-{item_name.lower().replace(" ", "-")}"]'
        self.click_element(remove_button)
        
    def remove_first_item_from_cart(self) -> None:
        """Remove first item from cart"""
        first_remove_btn = self.page.query_selector(self.REMOVE_BUTTONS)
        if first_remove_btn:
            first_remove_btn.click()
            
    def click_continue_shopping(self) -> None:
        """Click continue shopping button"""
        self.click_element(self.CONTINUE_SHOPPING_BUTTON)
        
    def click_checkout(self) -> None:
        """Click checkout button"""
        self.click_element(self.CHECKOUT_BUTTON)
        
    def is_cart_empty(self) -> bool:
        """Check if cart is empty"""
        return self.get_cart_items_count() == 0
        
    def verify_item_in_cart(self, item_name: str) -> bool:
        """Verify specific item is in cart"""
        cart_items = self.get_cart_item_names()
        return item_name in cart_items
