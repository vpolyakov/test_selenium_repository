
class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def open_p(self):
        self.driver.get('http://localhost/litecart/en/')
        return self

    def goto_product_page(self):
        self.driver.find_element_by_css_selector("#box-most-popular a.link").click()
        return self

    def goto_cart_page(self):
        self.driver.find_element_by_css_selector("#cart a.link").click()
        return self

    @property
    def quantity_of_products_in_cart(self):
        return int(self.driver.find_element_by_css_selector("span.quantity").text)
