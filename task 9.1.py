from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")

driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()


# проверить, что страны расположены в алфавитном порядке
countries = []
for row in driver.find_elements_by_css_selector("tr.row"):
    cell = row.find_elements_by_css_selector("td")[4]
    countries.append(cell.find_element_by_tag_name("a").text)

print('Количество стран=', len(countries))

if countries == sorted(countries):
    print("Страны отсортированы правильно\n")
else:
    print("Страны не отсортированны\n")


#  для тех стран, у которых количество зон отлично от нуля --
#  открыть страницу этой страны и там проверить, что зоны расположены в алфавитном порядке
country_count = len(driver.find_elements_by_css_selector("tr.row"))
for row_num in range(country_count):
    row = driver.find_elements_by_css_selector("tr.row")[row_num]
    if int(row.find_elements_by_css_selector("td")[5].text) != 0:
        print(row.find_elements_by_css_selector("td")[4].text)
        cell = row.find_elements_by_css_selector("td")[4]
        cell.find_element_by_tag_name("a").click()
        table_zones = driver.find_element_by_css_selector("table#table-zones")
        tz_rows = table_zones.find_elements_by_css_selector("tr")
        t_zones = []
        for k in range(1, len(tz_rows) - 1):
            name_zone_cell = tz_rows[k].find_elements_by_css_selector("td")[2]
            t_zones.append(name_zone_cell.text)
        if t_zones == sorted(t_zones):
            print("Зоны отсортированы правильно\n")
        else:
            print("Зоны не отсортированны\n")
        driver.back()


driver.quit()
