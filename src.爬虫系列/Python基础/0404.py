'''
作业4:选做(难易程度****)
请分别统计每个学生的总分和平均分，以字典的形式输出
score = {
    "张三":{"语文":90,"数学":85,"英语":92},
    "李四":{"语文":72,"数学":95,"英语":88},
    "王五":{"语文":85,"数学":78,"英语":90},
}
输出内容如下：
{"张三":{"总成绩":xxx,"平均成绩":xxx},"李四":{"总成绩":xxx,"平均成绩":xxx}....}
'''
score = {
    "张三":{"语文":90,"数学":85,"英语":92},
    "李四":{"语文":72,"数学":95,"英语":88},
    "王五":{"语文":85,"数学":78,"英语":90},
}
print(score.keys())
print(score.values())
print(score.items())
sc_dict = {}
for i,sc in score.items():
    print(i,sc)
    print("分数",sc.values())
    total=sum(sc.values())
    print(total)
    svg=total/len(sc)
    print(svg)
    sc_dict[i]={"总成绩":total,"平均分":svg}
print(sc_dict)








