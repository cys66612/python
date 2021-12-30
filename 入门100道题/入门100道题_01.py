#数字组合
num=0
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if((a!=b)and(b!=c)and(a!=c)):
                c=a*100+b*10+c
                print(c)
                num+=1
print(num)