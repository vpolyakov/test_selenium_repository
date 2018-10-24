from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product_to_cart(self):
        counter = int(self.driver.find_element_by_css_selector("span.quantity").text)

        if len(self.driver.find_elements_by_css_selector("select[name=options\\[Size\\]]")) > 0:
            select = self.driver.find_element_by_css_selector("select[name=options\\[Size\\]]")
            select.click()
            select.find_element_by_css_selector("option[value=Small]").click()

        self.driver.find_element_by_css_selector("[name=add_cart_product]").click()

        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), str(counter + 1)))
