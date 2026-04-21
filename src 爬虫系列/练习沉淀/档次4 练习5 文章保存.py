import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
}

response = requests.get(url, headers=headers)
data = response.json()

# 全量保存
with open("文章保存.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("练习5：全部文章保存完成")