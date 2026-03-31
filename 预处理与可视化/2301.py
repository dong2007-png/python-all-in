# from pyecharts.charts import Bar
#
# bar = Bar()
# bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90],color="green")
# # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# # 也可以传入路径参数，如 bar.render("mycharts.html")
# bar.render()
#各个国家的美食已经评分
from pyecharts.charts import Bar
bar = Bar()
bar.add_xaxis(["意大利披萨","中国火锅", "日本寿司", "法国法棍", "shit"])
bar.add_yaxis("各国美食",[6,9,5,3,8],color_by="data",bar_width=100)
bar.render("美食统计.html")

