# json数据格式实例没找到，省略
# 图片操作如下
import requests
fake_headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0"
}
url = "https://www.toopic.cn/public/uploads/image/20200411/20200411133329_21601.jpg"
response = requests.get(url, headers=fake_headers)
print(response.content)
with open("../images/toopic.jpg", "wb") as f:
    f.write(response.content)