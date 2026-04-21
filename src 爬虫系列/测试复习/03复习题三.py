import requests
import json
url="https://pic.rmb.bdstatic.com/bjh/3f138d1da2a/250312/f7c6c468cbb6e434b83c276396c52c4e.jpeg"
fake_headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    ,"referer":"https://yiqifu.baidu.com/g/aqc/index"
}

response=requests.get(url,headers=fake_headers)
with open("test.jpg","wb") as f:
    f.write(response.content)
