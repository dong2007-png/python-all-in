import pandas as pd
from pyecharts.charts import Bar
bar=Bar()
data=pd.read_excel("datas/01动物睡眠时间对比.xlsx")
print(data)
x_data=data["动物"]
print(x_data)
y_data=data["平均每日睡眠时间_小时"]
print(y_data)
x_data=x_data.tolist()
print("转换之后x轴的数据",x_data)

y_data=y_data.tolist()
print("转换之后y轴的数据",y_data)

bar.add_xaxis(x_data)
bar.add_yaxis("不同动物睡眠时长",y_data,color_by="data")
bar.render("animal.html")