"""
1. 网页源代码
2. json数据
3. 图片 视频 音频二进制数据
步骤
1. 发起请求 --> 对指定的url requests.get()/post()
2. 接受响应
3. 解析响应(获取里面的数据)
4. 保存
"""
import requests
import json   # json是python解释器自带的 不需要额外安装 直接可以导入使用
url = 'https://www.bkchina.cn/product/productList'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
}
"""
get(): 向指定的url发起get请求 并且获取服务器返回的响应数据
post(): 向指定的url发起post请求, post请求用于向服务器提交数据 post请求需要携带一个参数 data
data: 要发送给服务器的数据
user-agent:用户代理信息  如果缺少该信息 可能会被服务器拒绝访问或返回错误数据
"""
data = {'type': 'ham'}
response = requests.post(url=url, headers=headers, data=data)
# print(response.text)
print(type(response.text))  # <class 'str'> 字符串
# type(response.text) 查看response.text的类型
json_dict = json.loads(response.text)
print(json_dict)
# 想要操作数据, 就需要先懂数据的操作
result = json_dict['国王臻选']
for i in result:
    print(i['FName'])

result = json_dict['经典系列']
for i in result:
    print(i['FName'])