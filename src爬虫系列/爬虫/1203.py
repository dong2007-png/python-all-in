import requests
# 准备url
# 蒙德城角色json数据
url = "https://act-api-takumi-static.mihoyo.com/content_v2_user/app/16471662a82d418a/getContentList?iAppId=43&iChanId=727&iPageSize=50&iPage=1&sLangKey=zh-cn&iOrder=6"
# 构建请求头
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
}
# 发起请求
response = requests.get(url, headers=headers)
print(response.text)

url2 = 'https://act-api-takumi-static.mihoyo.com/content_v2_user/app/16471662a82d418a/getContentList?iAppId=43&iChanId=728&iPageSize=50&iPage=1&sLangKey=zh-cn&iOrder=6'
response = requests.get(url2, headers=headers)
print(response.text)