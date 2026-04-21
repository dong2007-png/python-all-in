import requests
import json

url = "https://jsonplaceholder.typicode.com/albums"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
}

response = requests.get(url, headers=headers)
data = response.json()

result = []
for item in data:
    result.append({
        "id": item["id"],
        "title": item["title"]
    })

with open("albums_simple.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("练习7：相册筛选保存完成")