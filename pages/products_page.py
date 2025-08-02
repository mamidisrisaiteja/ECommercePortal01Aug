"""
Products/Inventory Page Object Model
"""
from playwright.sync_api import Page
from pages.base_page import BasePage
from typing import List

class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        
    # Locators
    PRODUCTS_TITLE = '.title'
    PRODUCT_ITEMS = '.inventory_item'
    ADD_TO_CART_BUTTONS = '[data-test^="add-to-cart"]'
    CART_ICON = '.shopping_cart_link'
    CART_BADGE = '.shopping_cart_badge'
    SORT_DROPDOWN = '[data-test="product_sort_container"]'
    PRODUCT_NAMES = '.inventory_item_name'
    PRODUCT_PRICES = '.inventory_item_price'
    
    def verify_products_page_loaded(self) -> bool:
        """Verify that products page is loaded"""
        return self.is_element_visible(self.PRODUCTS_TITLE) and "Products" in self.get_text(self.PRODUCTS_TITLE)
        
    def verify_products_text_displayed(self) -> bool:
        """Verify 'Products' text is displayed"""
        return self.verify_page_contains_text("Products")
        
    def verify_add_to_cart_text_displayed(self) -> bool:
        """Verify 'Add to cart' text is displayed"""
        return self.verify_page_contains_text("Add to cart")
        
    def get_product_count(self) -> int:
        """Get the number of products displayed"""
        return len(self.page.query_selector_all(self.PRODUCT_ITEMS))
        
    def add_first_product_to_cart(self) -> None:
        """Add the first product to cart"""
        first_add_to_cart_btn = self.page.query_selector(self.ADD_TO_CART_BUTTONS)
        if first_add_to_cart_btn:
            first_add_to_cart_btn.click()
            
    def add_product_to_cart_by_name(self, product_name: str) -> None:
        """Add a specific product to cart by name"""
        product_button = f'[data-test="add-to-cart-{product_name.lower().replace(" ", "-")}"]'
        self.click_element(product_button)
        
    def click_cart_icon(self) -> None:
        """Click on cart icon"""
        self.click_element(self.CART_ICON)
        
    def get_cart_badge_count(self) -> str:
        """Get cart badge count"""
        if self.is_element_visible(self.CART_BADGE):
            return self.get_text(self.CART_BADGE)
        return "0"
        
    def sort_products_by_name_a_to_z(self) -> None:
        """Sort products by name A to Z"""
        self.click_element(self.SORT_DROPDOWN)
        self.page.select_option(self.SORT_DROPDOWN, "az")
        
    def sort_products_by_name_z_to_a(self) -> None:
        """Sort products by name Z to A"""
        self.click_element(self.SORT_DROPDOWN)
        self.page.select_option(self.SORT_DROPDOWN, "za")
        
    def sort_products_by_price_low_to_high(self) -> None:
        """Sort products by price low to high"""
        self.click_element(self.SORT_DROPDOWN)
        self.page.select_option(self.SORT_DROPDOWN, "lohi")
        
    def sort_products_by_price_high_to_low(self) -> None:
        """Sort products by price high to low"""
        self.click_element(self.SORT_DROPDOWN)
        self.page.select_option(self.SORT_DROPDOWN, "hilo")
        
    def get_product_names(self) -> List[str]:
        """Get list of all product names"""
        product_elements = self.page.query_selector_all(self.PRODUCT_NAMES)
        return [element.text_content() for element in product_elements]
        
    def verify_products_sorted_a_to_z(self) -> bool:
        """Verify products are sorted from A to Z"""
        product_names = self.get_product_names()
        return product_names == sorted(product_names)
        
    def verify_products_sorted_z_to_a(self) -> bool:
        """Verify products are sorted from Z to A"""
        product_names = self.get_product_names()
        return product_names == sorted(product_names, reverse=True)
