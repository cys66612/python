import easygui as g
import sys

while 1:
    g.msgbox("欢迎")
    msg="如果给你以下选择，你会选什么呢？"
    title="真心话大冒险"
    choices=["和美女谈恋爱", "陪富婆打游戏", "和好兄弟看电影"]
    choice=g.choicebox(msg,title,choices)

    g.msgbox("你的选择是："+str(choice),'结果')

    msg='你希望重新选择吗？'
    title='请作出你的选择'
    if g.ccbox(msg,title):
        pass
    else:
        sys.exit(0)
