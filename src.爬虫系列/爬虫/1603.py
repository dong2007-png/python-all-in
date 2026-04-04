from selenium.webdriver.edge.service import Service
from selenium import webdriver
import time
import urllib.request
from selenium.webdriver.common.by import By
service=Service("msedgedriver.exe")
browser=webdriver.Edge(service=service)
browser.get("https://bizhi1.com/item")
browser.maximize_window()
#滚动页面
for i in range(5):
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
time.sleep(3)
#滚动完毕寻找对应的标签
imgs=browser.find_elements(By.XPATH,'//img[contains(@class,"wp-post-image")]')
print(imgs)
count=0
for i in imgs:
    print(i.get_attribute('src.爬虫系列'))
    #请求
    filename=f"{count}.jpg"
    urllib.request.urlretrieve(i.get_attribute('src.爬虫系列'),filename)
    count+=1
time.sleep(5)
browser.quit()