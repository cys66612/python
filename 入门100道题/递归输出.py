def rec(string):
    if(len(string)!=1):
        rec(string[1:])
    print(string[0],end=' ')

string=input("string input:")
rec(string)
