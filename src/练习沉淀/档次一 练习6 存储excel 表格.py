import requests
from bs4 import BeautifulSoup
import pandas as pd

# 初始化列表
booknamelist = []
bookpricelist = []
bookpicturelist = []
bookdetaillist = []

# 只爬第 1 页
url = "https://books.toscrape.com/catalogue/page-1.html"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")

# 提取数据
for book in books:
    bookname = book.find("h3").find("a").get("title")
    booknamelist.append(bookname)

    bookprice = book.find("p", class_="price_color").text
    bookpricelist.append(bookprice)

    bookpicture = book.find("div", class_="image_container").find("a").find("img").get("src")
    bookpicturelist.append(bookpicture)

    bookdetail = book.find("h3").find("a").get("href")
    bookdetaillist.append(bookdetail)

# 保存 Excel
data = {
    "书名": booknamelist,
    "价格": bookpricelist,
    "书籍图片链接": bookpicturelist,
    "书籍详情": bookdetaillist
}

result = pd.DataFrame(data)
result.to_excel("书籍信息单页.xlsx", index=False)

print("书籍信息保存完毕")