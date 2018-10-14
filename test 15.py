from selenium import webdriver


driver1 = webdriver.driver = webdriver.Remote("http://192.168.0.44:4444/wd/hub", desired_capabilities={"browserName": "internet explorer"})
driver1.get("https://www.seleniumhq.org/projects/")
driver1.quit()

driver2 = webdriver.driver = webdriver.Remote("http://192.168.0.44:4444/wd/hub", desired_capabilities={"browserName": "chrome"})
driver2.get("https://www.seleniumhq.org/projects/")

driver2.quit()