import requests
import json
url="https://yiqifu.baidu.com/g/aqc/getDistrictAjax"
fake_headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    ,"referer":"https://yiqifu.baidu.com/g/aqc/index"
}
response=requests.get(url,headers=fake_headers)
json.loads(response.text)
print(json.loads(response.text))

