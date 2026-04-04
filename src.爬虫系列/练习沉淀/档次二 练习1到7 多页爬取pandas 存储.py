import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

booklist = []
a=int(input("请输入你要爬取的页数"))
for page in range(1, a+1):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    fake_headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
    }
    response=requests.get(f"https://books.toscrape.com/catalogue/page-{page}.html",headers=fake_headers)
    if response.status_code==200:

            soup=BeautifulSoup(response.text,"html.parser")
            books=soup.find_all("article",class_="product_pod")
            for book in books:
                bookpicture=book.find("div",class_="image_container").find("a").get("href")
                booktitle=book.find("h3").find("a").get("title")
                bookdetail=book.find("h3").find("a").get("href")
                bookprice=book.find("div",class_="product_price").find("p").text
                booklist.append([bookpicture,booktitle,bookdetail,bookprice])

    print(f"第{page}页爬取成功")

    time.sleep(random.randint(5,10))






result=pd.DataFrame(booklist,columns=["书籍图片详情","书籍名称","书籍详情","书籍价格"])
result.to_excel("书籍信息爬取.xlsx",index=False)
print("书籍总数：",len(booklist))
print("爬取完毕，文件保存成功")





