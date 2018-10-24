from selenium import webdriver

from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def open_main_page(self):
        self.main_page.open_p()

    def add_products(self, needed_products):
        while self.main_page.quantity_of_products_in_cart < needed_products:
            self.main_page.goto_product_page()
            self.product_page.add_product_to_cart()
            self.main_page.open_p()

    def goto_cart_page(self):
        self.main_page.goto_cart_page()

    def empty_cart(self):
        if self.cart_page.quantity_of_product_types > 1:
            self.cart_page.product_shotcut.click()
        for i in range(self.cart_page.quantity_of_product_types):
            cells_quantity_before = self.cart_page.cells_quantity
            self.cart_page.remove_product_from_cart()
            self.cart_page.waiting_for_cart_table_update(cells_quantity_before)

    def quit(self):
        self.driver.quit()
