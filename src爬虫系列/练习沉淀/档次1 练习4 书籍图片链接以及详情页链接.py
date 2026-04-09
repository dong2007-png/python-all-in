import requests
from bs4 import BeautifulSoup


url="https://books.toscrape.com/"
headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"

}

response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.text,"html.parser")
books=soup.find_all("article",class_="product_pod")
hreflist=[]
pagelist=[]
for book in books:
    picture=book.find("div",class_="image_container").find("img")
    hreflist.append(picture.get("src爬虫系列"))
    page=book.find("h3").find("a")
    pagelist.append(page.get("href"))
print(hreflist)
print(pagelist)
result=zip(hreflist,pagelist)
print(list(result))



