import requests
import  time
import random
from bs4 import BeautifulSoup
session=requests.Session()
url="http://httpbin.org/"
fake_headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
}
response=session.get(url,headers=fake_headers)
print(response.text)
