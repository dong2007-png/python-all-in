# 1. 导入依赖（固定写法，无需修改）
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType  # 用于主题美化

# ==============================================
# 2. 数据读取与处理（唯一需要你修改的核心部分）
# ==============================================
# 读取Excel数据，修改为你的文件路径
datas = pd.read_excel("datas/02消费结构.xlsx")
# 提取「分类列」和「数值列」，修改为你的Excel列名
data_pair = list(zip(datas["消费项目"], datas["月金额_元"]))
# 打印数据，验证格式是否正确（正式运行可删除）
print("数据格式验证：", data_pair)

# ==============================================
# 3. 初始化饼图（基础配置，按需修改）
# ==============================================
# 初始化：设置图表大小、主题（默认MACARONS马卡龙色，美观通用）
pie = Pie(
    init_opts=opts.InitOpts(
        width="1000px",  # 图表宽度
        height="700px",  # 图表高度
        theme=ThemeType.MACARONS  # 主题，可选：LIGHT/DARK/CHALK等
    )
)

# ==============================================
# 4. 核心：add() 数据与样式配置（覆盖80%场景）
# ==============================================
pie.add(
    # 4.1 必传参数：系列名 + 数据
    series_name="月度消费结构",  # 系列名，显示在图例/提示框
    data_pair=data_pair,  # 饼图核心数据，(名称,数值)列表

    # 4.2 饼图形状：环形/实心（通用环形，更美观）
    radius=["35%", "65%"],  # 内圈/外圈大小，传列表=环形，传字符串=实心
    center=["50%", "50%"],  # 饼图在画布中的位置，默认居中

    # 4.3 标签配置（最常用，专业饼图标配）
    label_opts=opts.LabelOpts(
        # 标签格式：分类名 + 金额 + 百分比，pyecharts固定占位符
        formatter="{b}: {c}元 ({d}%)",
        position="outside",  # 标签位置：outside(外侧)/inside(内侧)/center(中心)
        font_size=11,  # 字体大小
        font_weight="normal",  # 字体粗细
        color="#333"  # 字体颜色
    ),

    # 4.4 提示框配置（鼠标悬浮显示，默认优化）
    tooltip_opts=opts.TooltipOpts(
        trigger="item",
        formatter="{b}<br/>金额: {c}元<br/>占比: {d}%",  # 悬浮提示格式
        textstyle_opts=opts.TextStyleOpts(font_size=12)
    ),

    # 4.5 扇区样式（通用美化，可选）
    itemstyle_opts=opts.ItemStyleOpts(
        border_width=1,  # 扇区间隔边框宽度
        border_color="#fff",  # 边框颜色（白色，区分扇区）
        opacity=0.9  # 透明度
    )
)

# ==============================================
# 5. 全局配置：标题、图例、工具箱（专业图表必备）
# ==============================================
pie.set_global_opts(
    # 5.1 标题配置（居中，主副标题可选）
    title_opts=opts.TitleOpts(
        title="月度消费结构分析",
        subtitle="数据来源：个人账单",  # 副标题，可删除
        pos_left="center",
        pos_top="2%",
        title_textstyle_opts=opts.TextStyleOpts(font_size=18, font_weight="bold"),
        subtitle_textstyle_opts=opts.TextStyleOpts(font_size=12, color="#666")
    ),

    # 5.2 图例配置（左侧垂直排列，避免遮挡）
    legend_opts=opts.LegendOpts(
        pos_left="2%",
        pos_top="15%",
        orient="vertical",  # 垂直排列
        legend_icon="circle",  # 图例图标样式
        textstyle_opts=opts.TextStyleOpts(font_size=11)
    ),

    # 5.3 工具箱配置（下载图片、数据视图，汇报必备）
    toolbox_opts=opts.ToolboxOpts(
        is_show=True,
        pos_left="right",
        feature={
            "saveAsImage": {},  # 保存为图片
            "dataView": {},  # 查看原始数据
            "restore": {},  # 重置图表
            "dataZoom": {}  # 缩放（饼图可选）
        }
    )
)

# ==============================================
# 6. 渲染生成HTML文件（修改文件名即可）
# ==============================================
pie.render("02_消费结构饼图_完整版.html")
print("图表生成完成！请打开HTML文件查看效果。")