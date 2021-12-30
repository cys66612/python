#三数排序
raw2=[]
for i in range(3):
    x=int(input('输入你想要输入的数'))
    raw2.append(x)
raw2.sort()

for i in range(len(raw2)):
    print(raw2[i])