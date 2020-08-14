"""
创建多选复选框：vriable代表的是一个按钮的状态，一般0代表未激活，1代表激活
创建多选的话就要用多个tk变量
"""
# from tkinter import *
# root = Tk()
# 
# v =[]
# 
# GRILS = ["西施",
	# "王昭君",
	# "貂蝉",
	# "杨玉环"]
# 
# for g in GRILS:
    # v.append(IntVar())
    # b = Checkbutton(root,text=g,variable = v[-1],activebackground='GREEN',activeforeground='red')
    # b.pack(anchor='w')
# 
# mainloop()
"""
创建单选复选框
创建单选的话就要用到共用一个变量
"""
# from tkinter import *
# root = Tk()
# v = IntVar()       # 共用变量v
# GRILS = [("西施",1),
	# ("王昭君",2),
	# ("貂蝉",3),
	# ("杨玉环",4)]
# 
# for gril ,val in GRILS:
    # 说明：如果variable表示的是按钮的状态，
    #   如果这个按钮被点中了那么v就会被用val赋值，
    #   只有当variable = val的时候，才表示这个按钮处于激活状态
    # b = Radiobutton(root,text=gril,variable=v,value = val)
    # b.pack(anchor = W)
# mainloop()
# 
# 
from tkinter import *


root  = Tk()
var = StringVar()
def func(reason):
    if not reason.isdigit():
        text.delete(0,END)
        return False
    else:
        return True
    
    
    
    
    
funcCMD = root.register(func)   #   vcmd不是任何一个python函数就可以，必须是tk函数（通过root进行注册）
text= Entry(root,bg='yellow',#  设置背景颜色
    exportselection = True,
    insertbackground='red', #   设置光标颜色
    font=('楷体',12,'bold'),
    fg='green', #   设置字体颜色
    insertborderwidth=100,  #
    insertofftime=2000, #设置光标闪烁时间的间隔
    show=None,   #   设置要显示在文本框中的内容，设置密码的时候使用
    textvariable=var,    #将输入内容与tk变量绑定，
    validate='focusout', #   指定什么时候要进行验证输入的内容
    validatecommand = (funcCMD,'%P')  #   验证函数
    ) 
t = Entry(root)
t.pack()
text.pack()
mainloop()

print(type(var.get()))



