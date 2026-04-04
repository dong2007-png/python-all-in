#文本追加
import json

with open("../测试数据/毒鸡汤.txt", "r", encoding="utf-8") as file:
     content2=file.read()
     print(content2)
#json数据读取
with open("../测试数据/四大名著.json", "r", encoding="utf-8") as file:
     content=file.read()
     #content是字符串
     print(type(content))
     content3=json.loads(content)
     for item in content3:
          print(item['title'])
          