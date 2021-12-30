import easygui as g
m='【*真实姓名】为必填项。\n【*手机号码】为必填项。\n【*E-mail】为必填项。'
title='账号中心'
filednames=['*用户名','*真实姓名','固定电话','*手机号码','QQ','*E-mail']
fieldValues=g.multenterbox(m,title,filednames)
for i in range(len(filednames)):
    if '*' in filednames[i]:
        if fieldValues==[]:
            g.msgbox('带*号的为必填项，请重新填写')
            break