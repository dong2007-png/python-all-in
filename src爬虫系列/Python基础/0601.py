import random
data = {
    'def':'定义函数',
    'while':'不明确次数的循环',
    'for':'已知次数的循环',
    'return':'程序结束',
    'break':'跳出循环',
    'not':'逻辑非',
    'or':'逻辑或',
    'and':'逻辑和',
    'class':'定义类',
    'float':'浮点数标识符',
    'input':'用户输入',
    'dict':'字典标识符',
    'int':'整数类型标识符',
    'list':'列表标识符',
    'print':'打印输出',
    'bool':'布尔值标识符',
    'import':'导入模块'
}
for i in range(1,4):
    print(f"开始游戏,当前在第{i}关")
    jifen=0
    while True:
        word=random.choice(list(data.keys()))
        wordlen=len(word)
        if i<3:
            wordlist=list(word)   #先转为列表
            indexs=random.sample(range(len(wordlist)),i)
            for index in indexs:
                wordlist[index]="_"
            #转回字符串
            tishi="".join(wordlist)
        else:
            tishi=f"关键词长度为{wordlen}"
        print(f"题目:{data[word]}的关键词是")
        print(f"提示{tishi}")
        answer=input("请输入你的答案")
        if answer == word:
            jifen+=1
            print(f"恭喜你，目前的积分为{jifen}")
        else:
            print(f"很遗憾猜错了")
        if jifen==3:
            print(f"恭喜您通过本关，可进入下一关")
            break
    nextlevel=input("是否进入下一关")
    if nextlevel !="是":
        print("我不玩了，润")
        break

































