from tkinter import *
'''
单选的精髓就是：
    用一个val来表示按钮的状态
'''
root = Tk()
val = IntVar()
group= LabelFrame(root,text="最好的语言是:",padx=10,pady=10)
group.pack(anchor = 'w')
LANGE=[('python',1),
       ('php',2),
       ('lua',3)]
for lange, index in LANGE:
    b = Radiobutton(group,text = lange,variable = val , value = index)
    b.pack(anchor = 'nw',fill='y')
mainloop()





