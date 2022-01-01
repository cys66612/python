def draw(num):
    a="*"*(2*(4-num)+1)
    print(a.center(9,' '))
    #center返回一个长度为width,两边用fillchar(单字符)填充的字符串，即字符串str居中，两边用fillchar填充。若字符串的长度大于width,则直接返回字符串str
    if(num!=1):
        draw(num-1)
        print(a.center(9,' '))

draw(4)