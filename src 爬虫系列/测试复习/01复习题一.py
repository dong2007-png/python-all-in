import requests
from bs4 import BeautifulSoup
url="https://www.baidu.com/"
fake_headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0"
    ,"referer":"https://www.baidu.com/"
}
response = requests.get(url,headers=fake_headers)
list=[]
if response.status_code == 200:
    soup=BeautifulSoup(response.text,"html.parser")
    spans=soup.find_all("span",class_="title-content-title")
    for span in spans:
        print(span.text)
        list.append(span.text)
    print(list)
    