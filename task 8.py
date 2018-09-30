from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost/litecart/")
wait = WebDriverWait(driver, 10)  # seconds

products = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "li.product.column.shadow.hover-light")))
for product in products:
    if (len(product.find_elements_by_css_selector("div.sticker.new")) == 1 and
        not len(product.find_elements_by_css_selector("div.sticker.sale")) > 0) \
            or\
            (len(product.find_elements_by_css_selector("div.sticker.sale")) == 1 and
             not len(product.find_elements_by_css_selector("div.sticker.new")) > 0):
        print('Наличие одного стикера соблюдено', 'len_new=%d, len_sale=%d '
              % (len(product.find_elements_by_css_selector("div.sticker.new")),
                 len(product.find_elements_by_css_selector("div.sticker.sale"))))
    else:
        print('Невыплнение наличия одного стикера', 'len_new=%d, len_sale=%d '
              % (len(product.find_elements_by_css_selector("div.sticker.new")),
                 len(product.find_elements_by_css_selector("div.sticker.sale"))))

driver.quit()
