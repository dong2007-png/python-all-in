#字符串切片综合练习
#要求：
#定义一个名为 process_phone 的函数，接收一个字符串类型的手机号参数 phone（输入为 11 位纯数字手机号）：
#用字符串切片提取手机号的前三位以及后四位



def process_phone():
    phone=input("请输入你的手机号")
    print(phone[:3])
    print(phone[-1:-5:-1])
process_phone()


