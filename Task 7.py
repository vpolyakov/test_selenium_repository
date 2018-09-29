from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost/litecart/admin/")
wait = WebDriverWait(driver, 10)  # seconds

driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()


def upper_menus():
    return driver.find_elements_by_css_selector("ul#box-apps-menu li#app-")


wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul#box-apps-menu li#app-")))

kol_menu_items = len(upper_menus())

for i in range(kol_menu_items):
    upper_menus()[i].find_element_by_tag_name('a').click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    if len(upper_menus()[i].find_elements_by_tag_name('li')) > 1:
        for k in range(1, len(upper_menus()[i].find_elements_by_tag_name('li'))):
            upper_menus()[i].find_elements_by_tag_name('li')[k].find_element_by_tag_name('a').click()
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

driver.quit()
