import requests
fake_headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0"    ,
    "referer":"https://pic.netbian.com/tupian/38682.html"
}
url = "https://pic.netbian.com/uploads/allimg/250516/110318-17473645980a8c.jpg"
response = requests.get(url, headers=fake_headers)
print(response.content)
with open("../images/jianlai.jpg", "wb") as f:
    f.write(response.content)