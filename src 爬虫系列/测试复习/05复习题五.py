from selenium.webdriver.edge.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
service=Service("msedgedriver.exe")
browser=webdriver.Edge(service=service)
time.sleep(3)
#打开网页
browser.get("https://www.baidu.com/index.php?tn=68018901_58_oem_dg")
browser.maximize_window()
time.sleep(3)
#元素定位
#ID/class
btn=browser.find_element(By.ID,value="chat-submit-button")
print(btn)
time.sleep(3)
#xpath
textarea=browser.find_element(By.XPATH,'//textarea[@id="chat-textarea"]')
print(textarea)
time.sleep(3)
#输入文本框
textarea.send_keys("王者荣耀")
time.sleep(3)
btn.click()
time.sleep(3)
