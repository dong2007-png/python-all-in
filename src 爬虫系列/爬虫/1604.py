# 1.导入selenium库
from selenium.webdriver.chrome.service import Service # 导入浏览器驱动服务
from selenium import webdriver
import time
import urllib.request # python自带的请求库，是一个比较简单的请求库
# 导入查找模块
from selenium.webdriver.common.by import By
# 2.创建驱动实例来控制浏览器
service = Service("chromedriver.exe")

# 3.创建浏览器窗口
browser = webdriver.Chrome(service=service)
browser.maximize_window()
# 4.访问微博页面
browser.get("https://weibo.com/u/3261134763?tabtype=album")
time.sleep(3)
# 5.应该在访问到页面之后进行页面的滚动
for i in range(10):
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
# 6.滚动完毕之后寻找对应的标签 class=woo-picture-main woo-picture-square woo-picture-hover的div
divs = browser.find_elements(By.XPATH,'//div[@class="woo-picture-main woo-picture-square woo-picture-hover"]')
print("divs",divs) # [div,div,div,div.........]
count = 0 # 照片命名的变量
# 7.循环找到的所有div
for i in divs:
    count += 1
    img = i.find_element(By.XPATH,"./img")
    img_url = img.get_attribute("src") # 元素.get_attribute("属性名") == 属性值
    print("图片地址",img_url)
    # 拼接完整文件名
    file_name = f"刘亦菲/{count}.jpg"
    # 向地址发起请求
    urllib.request.urlretrieve(img_url,file_name) # urlretrieve函数的作用就是来下载一些小图片文件之类的....
time.sleep(5)

# requests他是没有页面的，如果风控比较严格，那么很大概率被发现
# selenium模拟真人
# 下节课: ip代理 ，验证码破解