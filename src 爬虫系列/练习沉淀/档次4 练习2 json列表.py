import requests
import json
url="https://jsonplaceholder.typicode.com/comments"
fake_headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
}
response = requests.get(url,headers=fake_headers)
data=response.json()
comments_list=[]
for item in data:
    comment={
        "名字" : item["name"],
        "邮件" : item["email"]
    }


    comments_list.append(comment)


print(comments_list)