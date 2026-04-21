score=int(input("请输入你的分数："))
if score>=90:
    print("优秀")
elif score>=80 and score<90:
    print("良好")
elif score>=70 and score<80:
    print("中等")
elif score>=60 and score<70:
    print("及格")
else:
    print("不及格")
