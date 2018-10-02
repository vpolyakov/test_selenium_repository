from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost/litecart/en/")


def products():
    campaigns = driver.find_element_by_css_selector("div#box-campaigns")
    return campaigns.find_elements_by_css_selector("li")


test_passed = True
for product_num in range(len(products())):
    product = products()[product_num]
    name = product.find_element_by_css_selector(".name").text
    print("%s:" % name)
    print("Главная страница:")
    if len(product.find_elements_by_css_selector("s.regular-price")) > 0:
        print('main regular price - striked = Yes')
    else:
        print('main regular price - striked = No')
        test_passed = False
    regular_price = product.find_element_by_css_selector(".regular-price")
    regular_price_color = regular_price.value_of_css_property("color")[5:-1].split(", ")

    if regular_price_color[0] == regular_price_color[1] and regular_price_color[1] == regular_price_color[2]:
        print("main regular price color's gray = Yes")
    else:
        print("main regular price color's gray = No")
        test_passed = False
    main_regular_price = regular_price.text
    if len(product.find_elements_by_css_selector("strong.campaign-price")) > 0:
        print('main campaign price has bold type = Yes')
    else:
        print('main campaign price has bold type = No')
        test_passed = False
    campaign_price = product.find_element_by_css_selector(".campaign-price")
    campaign_price_color = campaign_price.value_of_css_property("color")[5:-1].split(", ")

    if campaign_price_color[1] == "0" and campaign_price_color[2] == "0":
        print("main campaign price color's red = Yes")
    else:
        print("main campaign price color's red = No")
        test_passed = False
    main_campaign_price = campaign_price.text
    if float(campaign_price.value_of_css_property("font-size")[:-2]) > \
            float(regular_price.value_of_css_property("font-size")[:-2]):
        print("main campaign price font size's greater than regular = Yes")
    else:
        print("main campaign price font size's greater than regular = No")
        test_passed = False

    product.find_element_by_css_selector("a.link").click()

    # Карточка товара
    if driver.find_element_by_css_selector("h1").text == name:
        print("Название товара на главной странице совпадает с названием в карточке товара")
    else:
        print("Название товара на главной странице не совпадает с названием в карточке товара")
        test_passed = False

    if driver.find_element_by_css_selector(".regular-price").text == main_regular_price:
        print("Обычная цена на главной странице совпадает с ценой в карточке товара")
    else:
        print("Обычная цена на главной странице не совпадает с ценой в карточке товара")
        test_passed = False

    if driver.find_element_by_css_selector(".campaign-price").text == main_campaign_price:
        print("Акционная цена на главной странице совпадает с ценой в карточке товара")
    else:
        print("Акционная цена цена на главной странице не совпадает с ценой в карточке товара")
        test_passed = False

    print("Карточка товара:")

    if len(driver.find_elements_by_css_selector("s.regular-price")) > 0:
        print('regular price - striked = Yes')
    else:
        print('regular price - striked = No')
        test_passed = False
    regular_price = driver.find_element_by_css_selector(".regular-price")
    regular_price_color = regular_price.value_of_css_property("color")[5:-1].split(", ")

    if regular_price_color[0] == regular_price_color[1] and regular_price_color[1] == regular_price_color[2]:
        print("regular price color's gray = Yes")
    else:
        print("regular price color's gray = No")
        test_passed = False

    if len(driver.find_elements_by_css_selector("strong.campaign-price")) > 0:
        print('campaign price has bold type = Yes')
    else:
        print('campaign price has bold type = No')
        test_passed = False
    campaign_price = driver.find_element_by_css_selector(".campaign-price")
    campaign_price_color = campaign_price.value_of_css_property("color")[5:-1].split(", ")

    if campaign_price_color[1] == "0" and campaign_price_color[2] == "0":
        print("campaign price color's red = Yes")
    else:
        print("campaign price color's red = No")
        test_passed = False

    if float(campaign_price.value_of_css_property("font-size")[:-2]) > \
            float(regular_price.value_of_css_property("font-size")[:-2]):
        print("campaign price font size's greater than regular = Yes\n")
    else:
        print("campaign price font size's greater than regular = No\n")
        test_passed = False

    driver.back()

if test_passed:
    print('Поздравляю! Тест пройден успешно!')
else:
    print('К сожалению не все условия пройдены успешно. Тест провален.')

driver.quit()
