import requests
import json
url="https://www.bkchina.cn/product/productList"
fake_headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0",
    "referer":"https://www.bkchina.cn/product/hamburg.html"

}
data={
    'type':'ham'
}
response=requests.post(url,headers=fake_headers,data=data)
list1=json.loads(response.text)
print(list1)
print(type(list1))
print(list1["国王臻选"][0]["FName"])