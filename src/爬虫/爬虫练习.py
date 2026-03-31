import requests
from bs4 import BeautifulSoup
url="https://top.baidu.com/board?platform=pc&sa=pcindex_entry"
fake_headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
}
request = requests.get(url,headers=fake_headers)
print(request.status_code)
if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    res=soup.find_all("a",class_="c-single-text-ellipsis name_3SMKh")
    res_redu=soup.find_all("div",class_="hot-score-icon_1ve4d")
    for title,score in zip(res,res_redu):
        score=score.find("span").text
        print("------------------------------------------------------------------");
        print(f"标题:{title.text}--------------------热度；{float(score)}\t")





