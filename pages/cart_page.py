from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def quantity_of_product_types(self):
        return len(self.driver.find_elements_by_css_selector("[name=remove_cart_item]"))

    @property
    def product_shotcut(self):
        return self.driver.find_element_by_css_selector(".shortcut a")

    @property
    def cells_quantity(self):
        return len(self.driver.find_elements_by_css_selector(".dataTable td"))

    def remove_product_from_cart(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[name=remove_cart_item]"))).click()

    def waiting_for_cart_table_update(self, quantity_before):
        self.wait.until(lambda d: quantity_before - len(d.find_elements_by_css_selector(".dataTable td")) != 0)
