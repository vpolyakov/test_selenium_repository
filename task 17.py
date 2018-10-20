from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1)")

driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[title=Logout]")))

count = len(driver.find_elements_by_css_selector("a[title=Edit]"))
browser_logs = False
for i in range(2, count):
    driver.find_elements_by_css_selector("a[title=Edit]")[i].click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#tab-general")))

    if len(driver.get_log('browser')) > 0:
        browser_logs = True
        for j in driver.get_log('browser'):
            print(j)

    driver.back()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "form[name=search_form]")))

if not browser_logs:
    print('Логи браузера отсутствуют.')

driver.quit()
