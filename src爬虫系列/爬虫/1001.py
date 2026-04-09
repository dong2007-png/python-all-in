import requests

fake_headers="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"

url = "http://httpbin.org/get"

response = requests.get(url=url, headers=fake_headers)

print(response.text)
