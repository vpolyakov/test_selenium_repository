from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://localhost/litecart/en/")
wait = WebDriverWait(driver, 10)

for i in range(3):
    driver.find_element_by_css_selector("#box-most-popular a.link").click()
    counter = int(driver.find_element_by_css_selector("span.quantity").text)

    if len(driver.find_elements_by_css_selector("select[name=options\\[Size\\]]")) > 0:
        select = driver.find_element_by_css_selector("select[name=options\\[Size\\]]")
        select.click()
        select.find_element_by_css_selector("option[value=Small]").click()

    driver.find_element_by_css_selector("[name=add_cart_product]").click()

    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), str(counter + 1)))

    driver.back()

driver.find_element_by_css_selector("#cart a.link").click()

# Удаление товаров из корзины
kol_items = len(driver.find_elements_by_css_selector("[name=remove_cart_item]"))
if kol_items > 1:
    driver.find_element_by_css_selector(".shortcut a").click()

for k in range(kol_items):
    before = len(driver.find_elements_by_css_selector(".dataTable td"))
    driver.find_element_by_css_selector("[name=remove_cart_item]").click()

    # сравнение, изменилось ли что-то в таблице
    wait.until(lambda d: before - len(d.find_elements_by_css_selector(".dataTable td")) != 0)

driver.quit()
