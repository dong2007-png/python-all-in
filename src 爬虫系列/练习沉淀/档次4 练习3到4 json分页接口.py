import requests
import json  # 👉 这次必须导入！保存文件要用

url = "https://jsonplaceholder.typicode.com/posts"

fake_headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
}

response = requests.get(url, headers=fake_headers)
data = response.json()

# 👇 核心：把数据保存到本地 JSON 文件
with open("posts_all.json","w",encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False,indent=4)

print("全部文章已保存到 posts_all.json 成功！")