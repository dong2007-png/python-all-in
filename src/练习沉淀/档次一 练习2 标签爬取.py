import bs4
import requests


url="http://quotes.toscrape.com/"
headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0",

}
response = requests.get(url,headers=headers)
if response.status_code == 200:

    soup=bs4.BeautifulSoup(response.text,"lxml")
    print("解析后的数据",soup)

    textlist = []
    authorslist = []
    taglist = []
    texts = soup.find_all("span", class_="text")
    for text in texts:
        print(text.text)
        textlist.append(text.text)

    authors = soup.find_all("small", class_="author")
    for author in authors:
        print(author.text)
        authorslist.append(author.text)

    tags = soup.find_all("meta", class_="keywords")
    for tag in tags:
        print(tag.get("content"))
        taglist.append(tag.get("content"))

    zongjie=list(zip(textlist,authorslist,taglist))
    print(zongjie)


    #这里没有一起打包，直接zip可能有错位，下次注意
