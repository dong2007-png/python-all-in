#实战演练https://mesh.if.iqiyi.com/portal/pcw/rankList/comSecRankList?v=13.124.24146&device=c874b97822af8b1efda1677f3fb46a24&auth=&uid=&ip=202.108.14.240&refresh=0&server=false&page_st=0&tag=0&category_id=-1&channelId=0&date=&pg_num=1&version=13.124.24146
import json
import requests
url="https://mesh.if.iqiyi.com/portal/pcw/rankList/comSecRankList?v=13.124.24146&device=c874b97822af8b1efda1677f3fb46a24&auth=&uid=&ip=202.108.14.240&refresh=0&server=false&page_st=0&tag=0&category_id=-1&channelId=0&date=&pg_num=1&version=13.124.24146"
fakeheaders = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/53"
}
response = requests.get(url,headers=fakeheaders)
if response.status_code == 200:
    print(response.text)
    print(type(response.text))
    res=json.loads(response.text)
    print(type(json))
    print(res)
    for i in res["data"]["items"]:
        for content in i["contents"]:
            print(content["title"])






