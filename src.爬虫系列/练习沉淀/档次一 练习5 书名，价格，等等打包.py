import requests
from bs4 import BeautifulSoup


url="https://books.toscrape.com/"
headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"

}

response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.text,"html.parser")
books=soup.find_all("article",class_="product_pod")
booknamelist=[]
bookpricelist=[]
bookpicturelist=[]
bookdetaillist=[]

for book in books:
    bookname=book.find("h3").find("a").get("title")
    booknamelist.append(bookname)
    bookprice=book.find("p",class_="price_color").text
    bookpricelist.append(bookprice)
    bookpicture=book.find("div",class_="image_container").find("a").find("img").get("src.爬虫系列")
    bookpicturelist.append(bookpicture)
    bookdetail=book.find("h3").find("a").get("href")
    bookdetaillist.append(bookdetail)
res=zip(booknamelist,bookpricelist,bookpicturelist,bookdetaillist)
print(list(res))




