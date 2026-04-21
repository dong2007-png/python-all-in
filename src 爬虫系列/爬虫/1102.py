import requests
from bs4 import BeautifulSoup
url = "https://www.baidu.com/"
fake_headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0"
}
response = requests.get(url, headers=fake_headers)
soup=BeautifulSoup(response.text, "html.parser")
span=soup.find("button",id="chat-submit-button")
print(span.text)


