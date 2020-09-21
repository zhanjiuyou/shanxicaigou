#  这块来构建我们的图形界面，让使用更方便
from tkinter import *


# 创建图形界面
mygui = Tk()
# 设置界面标题
mygui.title('第一个项目')
# 设置界面尺寸
mygui.geometry('600x500')
# 创建一个主菜单，然后里面包含其他小菜单。
def daying():
    print('heh')
menu = Menu(mygui)
fmenu1=Menu(mygui)
for item in ['新建','打开','保存','另存为']:
    # 如果该菜单是顶层菜单的一个菜单项，则它添加的是下拉菜单的菜单项。则他添加的是下拉菜单的菜单项。
    fmenu1.add_command(label=item,command=daying())

fmenu2=Menu(mygui)
for item in ['复制','粘贴','剪切']:
    fmenu2.add_command(label=item)

fmenu3=Menu(mygui)
for item in ['大纲视图','web视图']:
    fmenu3.add_command(label=item)

fmenu4=Menu(mygui)
for item in ["版权信息","其它说明"]:
    fmenu4.add_command(label=item)
menu.add_cascade(label='开始',menu=fmenu1)
menu.add_cascade(label='关于',menu=fmenu2)
#小的菜单项
mygui.config(menu=menu)





mainloop()