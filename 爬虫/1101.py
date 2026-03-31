import requests
url = "https://www.baidu.com/"
fake_headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0"
}
response = requests.get(url, headers=fake_headers)
with open("百度首页.html", "w", encoding="UTF-8") as f:
    f.write(response.text)

