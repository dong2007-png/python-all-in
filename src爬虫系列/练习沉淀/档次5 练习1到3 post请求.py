import requests
from bs4 import BeautifulSoup

login_url = "http://quotes.toscrape.com/login"
session = requests.Session()

response = session.get(login_url)
soup = BeautifulSoup(response.text, "html.parser")
csrf_token = soup.find("input", {"name": "csrf_token"})["value"]


login_data = {
    "csrf_token": csrf_token,
    "username": "test_user",
    "password": "test_password"
}

response = session.post(login_url, data=login_data)

# 验证登录成功（页面中会出现 "Logout"）
if "Logout" in response.text:
    print("✅ 登录成功！")
else:
    print("❌ 登录失败！")

