"""
作业3:必做(难易程度**)
有字典 dic = {"k1": "v1", "k2": "v2", "k3": "v3"}，实现以下功能：
(1)输出字典中所有的key
(2)输出字典中所有的value
(3)添加一个键值对"k4","v4",输出添加后的字典 dic
(4)删除字典 dic 中的键值对"k1","v1",并输出删除后的字典 dic
(5)获取字典 dic 中“k2”对应的值
"""

dic = {"k1": "v1", "k2": "v2", "k3": "v3"}
keys=dic.keys()
print(keys)
values=dic.values()
print(values)
dic["k4"]="v4"
print(dic)
del dic["k1"]
print(dic)
print(dic["k2"])
