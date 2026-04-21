for i in range(1,50):
    if i % 3 == 0 and i % 5 == 0:
        continue
    elif i % 3 == 0 and i % 5 != 0:
        print(i)

print("=====================================================")


for i in range(1,50):
    if i %5==0:
        continue
    if i % 3 == 0:
        print(i)

