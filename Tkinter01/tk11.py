from tkinter import *
root = Tk()
aritcl = Label(root,text="作品").grid(row = 0 ,column = 0)
author = Label(root, text =" 作者").grid(row = 1,column = 0)

e1 =Entry(root)
e2 = Entry(root)

e1.grid(row = 0,column = 1 , padx = 10,pady = 10)
e2.grid(row = 1,column = 1,padx = 10 ,pady = 10)
def show():
    print('作品《%s》'%e1.get())
    print('作者：%s'%e2.get())
    e1.delete(0,END)
    e2.delete(0,END)
    

look = Button(root,text="获取信息",width = 10,command = show)
look.grid(row = 3,column = 0 ,sticky = 'w',padx = 10 ,pady = 10)

q = Button(root, text="退出",width = 10,command =root.quit)
q.grid(row = 3,column = 1,sticky = 'e', padx = 10 ,pady = 10)

mainloop()

