import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
url="http://quotes.toscrape.com/"
fake_headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
}
response = requests.get(url,headers=fake_headers)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    biaoqians=soup.find_all("div",class_="quote")
    list=[]
    for biaoqian in biaoqians:

        biaoti=biaoqian.find("div",class_="tags").find("meta").get("content")
        # print(biaoti)
        quote=biaoqian.find("span",class_="text").text
        # print(quote)
        zuozhe=biaoqian.find("small",class_="author").text
        # print(zuozhe)
        lianjie=biaoqian.find("a").get("href")
        # print(lianjie)
        list.append([
            biaoti,quote,zuozhe,lianjie,
        ])


    with open("名言存储.csv","w",encoding="utf-8-sig") as f:
        writer = csv.writer(f,delimiter="\t")
        writer.writerow(["标签","名言","作者","链接"])
        writer.writerows(list)


    with open("名言存储.csv", "r", encoding="utf-8-sig") as f:
        print("csv保存完毕")
        a=csv.reader(f,delimiter="\t")
        print(a)
        for row in a:
            print(row)






