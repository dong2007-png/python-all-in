#文本读取操作

import requests
url="https://www.baidu.com/index.php?tn=75144485_1_dg&ch=9"
fakeheaders={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"



}
response = requests.get(url,headers=fakeheaders)
with open("百度首页.html", "w", encoding="utf-8") as f:
    f.write(response.text)

