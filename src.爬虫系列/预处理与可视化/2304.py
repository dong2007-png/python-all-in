import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie
datas=pd.read_excel("datas/02消费结构.xlsx")
data_pair=list(zip(datas["消费项目"],datas["月金额_元"]))
print(data_pair)
pie=Pie()
pie.add(
    "消费结构",
    data_pair=data_pair,
    label_opts=opts.LabelOpts(
        formatter="{b}:{c}元,{d}%"
    )

)
pie.set_global_opts(
    title_opts=opts.TitleOpts(
        title="消费结构分析",
        pos_left="center"
    ),
    legend_opts=opts.LegendOpts(
        pos_left="left",
        orient="vertical",
    )
)

pie.render("02_pie.html")
