import pandas as pd
from pyecharts.charts import Pie
from pyecharts import options as opts
data = pd.read_excel("datas/02消费结构.xlsx")
res1=data["消费项目"]
res2=data["月金额_元"]
print(res1)
print(res2)
res3=zip(res1,res2)
print(res3)
res4=list(res3)
print(res4)
pie = Pie()
pie.add(
    "消费结构",
    data_pair=res4,
    label_opts=opts.LabelOpts(
        formatter="{b}:{c}元{d}%"
    )
)
pie.render("消费结构pie.html")