from selenium.webdriver.edge.service import Service
from selenium import webdriver
import time

service = Service("msedgedriver.exe")

browser = webdriver.Edge(service=service)
browser.get("http://www.baidu.com")
time.sleep(10)
