from tkinter import *

root = Tk()
v = IntVar()
"""

单选，单项选择题：
    Radiobutton

"""
Radiobutton(root,text='西施',variable=v,value=1).pack(anchor='w')
Radiobutton(root,text='貂蝉',variable=v,value=2).pack(anchor='w')
Radiobutton(root,text='王昭君',variable=v,value=3).pack(anchor='w')
Radiobutton(root,text='杨玉华',variable=v,value=4).pack(anchor='w')

mainloop()
