from tkinter import *
"""
密码输入框，Entry中的show

"""


root = Tk()
aritcl = Label(root,text="账号").grid(row = 0 ,column = 0)
author = Label(root, text =" 密码").grid(row = 1,column = 0)

e1 =Entry(root)
e2 = Entry(root,show='*')

e1.grid(row = 0,column = 1 , padx = 10,pady = 10)
e2.grid(row = 1,column = 1,padx = 10 ,pady = 10)
def show():
    print('账号：%s'%e1.get())
    print('密码：%s'%e2.get())
    e1.delete(0,END)
    e2.delete(0,END)
    

look = Button(root,text="芝麻开门",width = 10,command = show)
look.grid(row = 3,column = 0 ,sticky = 'w',padx = 10 ,pady = 10)

q = Button(root, text="退出",width = 10,command =root.quit)
q.grid(row = 3,column = 1,sticky = 'e', padx = 10 ,pady = 10)

mainloop()

