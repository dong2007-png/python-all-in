import requests


session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0"
}

# ====================== 1. 爬网页：HTML → text ======================
print("===== 1. HTML（网页文字） =====")
url_html = "https://httpbin.org/html"
res = session.get(url_html, headers=headers)
print(res.text[:200])  # 有 <> 标签，文字页面


# ====================== 2. 拿数据：JSON → json() ======================
print("\n===== 2. JSON（接口数据，登录用这个） =====")
url_json = "https://httpbin.org/json"
res = session.get(url_json, headers=headers)
data = res.json()  # 纯数据，没有标签
print(data)


# ====================== 3. 下图片：二进制 → content ======================
print("\n===== 3. 二进制（图片/文件） =====")
url_img = "https://www.baidu.com/favicon.ico"  # 百度小图标
res = session.get(url_img, headers=headers)

# 保存图片
with open("favicon.ico", "wb") as f:
    f.write(res.content)

print("图片下载完成！")