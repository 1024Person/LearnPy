from tkinter import *


root = Tk()
root.title('成神之路')
v =IntVar()
b = Checkbutton(root,text="测试一下下",
           variable = v)
b.pack()
l = Label(root,text='选择状态',textvariable=v)
l.pack(side = "bottom")
mainloop()




