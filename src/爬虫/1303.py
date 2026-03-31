#表格数据读取，csv
import csv
with open("../测试数据/四大名著.csv", "r", encoding="gbk") as f:
    content = csv.reader(f)
    print(content)
    for i in content:
        print(i)
