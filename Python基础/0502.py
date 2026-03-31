#定义一个名为 rectangle_area 的函数，计算矩形面积：
#接收两个参数 width（宽度）和 height（高度），其中 height 设置默认值为 5；
#函数内部判断参数是否为正数（大于 0），如果不是则返回提示字符串 “参数必须为正数”；
#如果是正数则返回面积（宽 × 高）
def  rectangle_area(width, height):
    height = 5
    if width > 0:
        return width * height
    else:
        print("参数必须为正数")

area=rectangle_area(100, 100)
print(area)
rectangle_area(-100, 100)