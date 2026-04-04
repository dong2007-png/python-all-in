import requests
from bs4 import BeautifulSoup

url="http://quotes.toscrape.com/"

fake_headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
}

response = requests.get(url,headers=fake_headers)
staues=response.status_code
if staues==200:
    soup=BeautifulSoup(response.text,"lxml")
    print("解析后的数据",soup)
    textlist=[]
    authorslist=[]
    texts=soup.find_all("span",class_="text")
    for text in texts:
        print(text.text)
        textlist.append(text.text)

    authors=soup.find_all("small",class_="author")
    for author in authors:
        print(author.text)
        authorslist.append(author.text)


    dabao=zip(textlist,authorslist)
    print(list(dabao))


