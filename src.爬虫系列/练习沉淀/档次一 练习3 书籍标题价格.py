import requests
from bs4 import BeautifulSoup


url="https://books.toscrape.com/"
headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
}

response=requests.get(url,headers=headers)
soup=BeautifulSoup(response.text,"html.parser")
books=soup.find_all("article",class_="product_pod")
pricelist=[]
titlelist=[]
response.encoding = "utf-8"


for book in books:
    price=book.find("p",class_="price_color")
    pricelist.append(price.text)
    title=book.find("h3").find("a")
    titlelist.append(title.text)



dabao=list(zip(pricelist,titlelist))
print(dabao)







