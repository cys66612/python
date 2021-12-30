string=input("请输入你想要输入的字符串:")
alp=0
num=0
spa=0
oth=0

for i in range(len(string)):
    if string[i].isspace():
        spa+=1
    elif string[i].isdigit():#检查是否为十进制数字
        num+=1
    elif string[i].isalpha():#检查是否是英文单词，大写1，小写2，不是0
        alp+=1
    else:
        oth+=1

print("space:",spa)
print("digit:",num)
print("alpha:",alp)
print("other:",oth)
