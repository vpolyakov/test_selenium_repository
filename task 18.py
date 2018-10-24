from selenium import webdriver
from browsermobproxy import Server
import time


server = Server("C:\\Chromedriver\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy")
server.start()
proxy = server.create_proxy()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--proxy-server={0}".format(proxy.proxy))
driver = webdriver.Chrome(chrome_options=chrome_options)

proxy.new_har("google")
# driver.get("http://www.google.co.uk")
driver.get("http://software-testing.ru")
print(proxy.har)  # returns a HAR JSON blob

time.sleep(3)

server.stop()
