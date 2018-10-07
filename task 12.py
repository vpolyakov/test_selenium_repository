from selenium import webdriver
import os
import time

driver = webdriver.Chrome()
driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")

driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()

driver.find_elements_by_css_selector("a.button")[1].click()

# Заполнение вкладки General
driver.find_elements_by_css_selector("input[name=status]")[0].click()
driver.find_element_by_css_selector("input[name=name\\[en\\]]").send_keys("Пара уточек")
driver.find_element_by_css_selector("input[name=code]").send_keys("2ds")
driver.find_element_by_css_selector("input[data-name=Root]").click()
driver.find_element_by_css_selector("input[data-name='Rubber Ducks']").click()
driver.find_element_by_css_selector("input[name=quantity]").clear()
driver.find_element_by_css_selector("input[name=quantity]").send_keys("25.00")
sel_sold = driver.find_element_by_css_selector("select[name=sold_out_status_id]")
sel_sold.click()
sel_sold.find_elements_by_css_selector("option")[2].click()

path = os.getcwd() + "\\" + "pair_of_resin_ducks.jpg"
driver.find_element_by_css_selector("input[name=new_images\\[\\]]").send_keys(path)


tabs = driver.find_elements_by_css_selector("div.tabs li")

tabs[1].click()
time.sleep(1)
# заполнение вкладки Information
sel_mr = driver.find_element_by_css_selector("select[name=manufacturer_id]")
sel_mr.click()
sel_mr.find_elements_by_css_selector("option")[1].click()
driver.find_element_by_css_selector("input[name=short_description\\[en\\]]").send_keys("Две резиновые уточки")
driver.find_element_by_css_selector("textarea[name=description\\[en\\]]").send_keys("Много разных хороших уточек")


time.sleep(1)
tabs[3].click()
# заполнение вкладки Prices
driver.find_element_by_css_selector("input[name=purchase_price]").clear()
driver.find_element_by_css_selector("input[name=purchase_price]").send_keys("15.00")
driver.find_element_by_css_selector("input[name=prices\\[USD\\]]").send_keys("50")

driver.find_element_by_css_selector("button[name=save]").click()

# проверка нахождения введеного товара в базе
driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")

product_rows = driver.find_elements_by_css_selector(".dataTable tr.row")
product_finding = False
for row in product_rows:
    product_name = row.find_elements_by_css_selector("td")[2].find_element_by_css_selector("a").text
    if product_name == "Пара уточек":
        product_finding = True
        break

if product_finding:
    print("\nПроверка удалась! - добавленный товар появился в каталоге.")
else:
    print("\nНеудача! - добавленный товар не появился в каталоге.")

driver.quit()
