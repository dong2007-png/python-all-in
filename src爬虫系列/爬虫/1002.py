import requests
url='https://pic.netbian.com/tupian/39902.html'
fake_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0"
}
reponse = requests.get(url=url, headers=fake_headers,timeout=10)
reponse.encoding='gbk'
with open("../前端html基础/netbian.html", "w", encoding="gbk") as f:
    f.write(reponse.text)