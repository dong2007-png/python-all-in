start=int(input("请输入一个起始值"))
end = int(input("请输入一个结束值"))

jishu=0
oushu=0
for i in range(start, end+1):
    if i % 2 == 0:
        oushu += 1
    else :
        jishu += 1
print(f"奇数的个数为{jishu}")
print(f"偶数的个数为{oushu}")