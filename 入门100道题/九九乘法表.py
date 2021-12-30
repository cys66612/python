#九九乘法表
for i in range(1,10):
    for j in range(1,10):
        print('%d*%d=%2ld '%(i,j,i*j),end='')
    print()