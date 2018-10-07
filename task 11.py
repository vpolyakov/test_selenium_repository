from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd


driver_persons = webdriver.Chrome()
driver_persons.get("https://www.fakenamegenerator.com")
wait_person = WebDriverWait(driver_persons, 10)

driver = webdriver.Chrome()
driver.get("http://localhost/litecart/en/create_account")
wait = WebDriverWait(driver, 10)


# блок получения сгенерированных на стороннем сайте данных нового пользователя
# с проверкой на уже существование этого нового пользователя

# открытие файла базы с уже существующими пользователями
try:
    users_df = pd.read_csv('users.csv', index_col=['email'])
except FileNotFoundError:
    users_df = pd.DataFrame(columns=['password'])
    users_df.index.name = "email"

# получение данных нового пользователя
while True:
    wait_person.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#genbtn"))).click()
    name = wait_person.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".address h3"))).text.split()
    address = driver_persons.find_element_by_css_selector(".adr").text
    adr = address.split("\n")
    address1 = adr[0]
    print(address1)
    city = adr[1].split(", ")[0]
    print(city)
    state = adr[1].split(", ")[1].split(' ')[0]
    print(state)
    postcode = adr[1].split(", ")[1].split(' ')[1]
    print(postcode)
    first_name = name[0]
    print(first_name)
    last_name = name[2]
    print(last_name)
    extras = driver_persons.find_element_by_css_selector(".extra").find_elements_by_css_selector("dl")
    phone = '+1 ' + extras[3].find_element_by_css_selector("dd").text
    print(phone)
    email = extras[8].find_element_by_css_selector("dd").text.split("\n")[0]
    print(email)
    password = extras[10].find_element_by_css_selector("dd").text
    print(password)
    if email not in users_df.index:
        break

# передача данных нового пользователя на страницу регистрации
driver.find_element_by_name("firstname").send_keys(first_name)
driver.find_element_by_name("lastname").send_keys(last_name)
driver.find_element_by_name("address1").send_keys(address1)
driver.find_element_by_name("postcode").send_keys(postcode)
driver.find_element_by_name("city").send_keys(city)

driver.find_element_by_css_selector(".select2-selection__rendered").click()
driver.find_element_by_css_selector(".select2-search__field").send_keys("United States" + Keys.ENTER)

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[name=zone_code] option[value=%s]" % state))).click()

driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_name("phone").send_keys(phone)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_name("confirmed_password").send_keys(password)

driver.find_element_by_name("create_account").click()
users_df.loc[email] = [password]

wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Logout"))).click()

# сохранение пользователей в файл и закрытие генератора
users_df.to_csv("users.csv")
driver_persons.quit()


# Залогинивание и выход
driver.find_element_by_css_selector("input[name=email]").send_keys(email)
driver.find_element_by_css_selector("input[name=password]").send_keys(password)
driver.find_element_by_css_selector("button[name=login]").click()
driver.find_element_by_link_text("Logout").click()


driver.quit()
