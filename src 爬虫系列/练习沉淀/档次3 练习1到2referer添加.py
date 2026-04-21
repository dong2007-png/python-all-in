import requests
from bs4 import BeautifulSoup
url="https://httpbin.org/get"
fake_headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0",
    "referer":"https://httpbin.org/get"
}
response = requests.get(url,headers=fake_headers)
if response.status_code == 200:
    print(response.text)

