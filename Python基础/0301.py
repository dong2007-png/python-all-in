import random
count=10
number=1
jiangjin=0

jp=["10"]*10+["20"]*6+["30"]*2+["40"]*3+["50"]*2+["炸弹"]*10+["5"]*5+["6"]*6
print("======================抽奖游戏=====================")
print("======================现在开始=====================")
print(f"你一共有{count}次抽奖机会，抽奖满一百元可以提现，抽到炸弹奖金清零，中途可以选择放弃")


while count>0:


    xuanze=input("您是否选择开始游戏（选择是或否，不要打多余空格）")
    print(f"这是你第{number}次抽奖,还剩{count-1}次机会")

    if xuanze=="是" or xuanze=="shi":
        my_jp = random.choice(jp)
        print(f"本次抽奖结果是{my_jp}")
        if my_jp=="炸弹":
            jiangjin=0
            if number==1:
                print("你无敌了孩子，第一次就能抽到炸弹~~~")
            else :
                print(f"恭喜你在第{number}次游戏结束,您的奖金归零，赌狗！！！，重启接着玩哦~~~")
            break
        else:
            jiangjin+=int(my_jp)
            count-=1
            print(f"您的累计金额是{jiangjin}元，您还剩{count}次抽奖机会")
            if(jiangjin >=100):
                jp=["炸弹"]*100
                xuanze2=input("您现在累计金额大于等于一百，可以选择提现")
                if xuanze2=="选择提现" :
                    print(f"您已成功提现{jiangjin}元，祝您生活愉快~~~")
                    break
                else :
                    print("您选择继续游戏，后续可以选择提现，祝老板发发发~~~")


            else:
                print("您目前没有提现资格，继续游戏累计提现吧")
            number+=1


    elif xuanze =="fou" or xuanze == "否":
        print(f"游戏结束，您的累计金额是{jiangjin}元")
        break

    else:
        print("输入无效，请输入是或否")
if count==0:
    print(f"所有的抽奖机会都已用完，您目前累计金额是{jiangjin}元")


