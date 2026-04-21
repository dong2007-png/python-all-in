import requests
import json

url = "https://jsonplaceholder.typicode.com/comments"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
}

response = requests.get(url, headers=headers)
data = response.json()

# 先筛选，只保留需要的字段
result = []
for item in data:
    result.append({
        "email": item["email"],
        "body": item["body"]
    })

# 保存筛选后的数据
with open("comments_simple.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("练习6：评论筛选保存完成")