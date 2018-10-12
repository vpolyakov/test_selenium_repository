from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
wait = WebDriverWait(driver, 10)

driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()

driver.find_element_by_css_selector(".button").click()


def any_window_other_than(old_windows):
    def wrapper(d):
        handles = set(d.window_handles) - set(old_windows)
        if len(handles) > 0:
            return list(handles)[0]
        else:
            return False
    return wrapper


main_win = driver.current_window_handle

for i in range(len(driver.find_elements_by_css_selector("#content table [target=_blank]"))):
    all_old_win = driver.window_handles
    driver.find_elements_by_css_selector("#content table [target=_blank]")[i].click()
    new_window = wait.until(any_window_other_than(all_old_win))
    driver.switch_to.window(new_window)
    driver.close()
    driver.switch_to.window(main_win)

driver.quit()
