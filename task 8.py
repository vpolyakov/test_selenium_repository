from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost/litecart/")
wait = WebDriverWait(driver, 10)  # seconds

products = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "li.product")))
for product in products:
    if len(product.find_elements_by_css_selector("div.sticker")) == 1:
        print('Наличие только одного стикера соблюдено')
    else:
        print('Невыплнение наличия одного стикера')

driver.quit()
