from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")

driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()


def geo_rows():
    geo_z_table = driver.find_element_by_css_selector("table.dataTable")
    rows = geo_z_table.find_elements_by_css_selector("tr.row")
    return rows


for row_num in range(len(geo_rows())):
    cell = geo_rows()[row_num].find_elements_by_css_selector("td")[2]
    print(cell.find_element_by_tag_name("a").text)
    cell.find_element_by_tag_name("a").click()

    table_zones = driver.find_element_by_css_selector("table#table-zones")
    tz_rows = table_zones.find_elements_by_css_selector("tr")
    t_zones = []
    for k in range(1, len(tz_rows) - 1):
        name_zone_cell = tz_rows[k].find_elements_by_css_selector("td")[2]
        select_zone_box = name_zone_cell.find_element_by_tag_name("select")
        selected_zone = select_zone_box.find_element_by_css_selector("option[selected=selected]")
        t_zones.append(selected_zone.text)
    print(t_zones)
    if t_zones == sorted(t_zones):
        print("Зоны отсортированы правильно\n")
    else:
        print("Зоны не отсортированны\n")

    driver.back()

driver.quit()
