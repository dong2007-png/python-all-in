import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

booknamelist = []
bookpricelist = []
bookpicturelist = []
bookdetaillist = []
a=int(input("请输入你要爬取的页数"))
for page in range(1,a+1):
#网站初始化
        url=f"https://books.toscrape.com/catalogue/page-{page}.html"
        headers={
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0",
        }
        response=requests.get(url,headers=headers)
        soup=BeautifulSoup(response.text,"html.parser")
        books=soup.find_all("article",class_="product_pod")

#书籍信息抓取
        for book in books:
            bookname=book.find("h3").find("a").get("title")
            booknamelist.append(bookname)
            bookprice=book.find("p",class_="price_color").text
            bookpricelist.append(bookprice)
            bookpicture=book.find("div",class_="image_container").find("a").find("img").get("src爬虫系列")
            bookpicturelist.append(bookpicture)
            bookdetail=book.find("h3").find("a").get("href")
            bookdetaillist.append(bookdetail)

        print(f"正在爬{page}页")
        time.sleep(5)

#最终存储
res=zip(booknamelist,bookpricelist,bookpicturelist,bookdetaillist)
print(list(res))
data={
        "书名":booknamelist,
        "价格":bookpricelist,
        "书籍图片链接":bookpicturelist,
        "书籍详情":bookdetaillist,
    }
result=pd.DataFrame(data)
result.to_excel("书籍信息多页.xlsx",index=False)

print("数据条数：", len(booknamelist))
print(result.head())
input("按回车退出...")
print("书籍信息保存完毕")
print("文件真实路径：", os.path.abspath("书籍信息多页.xlsx"))