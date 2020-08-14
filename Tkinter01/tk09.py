"""

多选题：checkbutton()

"""

from tkinter import *
GRILS=["西施",
       '貂蝉',
       '王昭君',
       '杨玉环']
root = Tk()
v= []
for grils in GRILS:
    v.append(IntVar())
    c = Checkbutton(root,text=grils,variable=v[-1])
    c.pack(anchor = 'w')
for i in v:
    l = Label(root,textvariable = i)
    l.pack(anchor = 'n')
mainloop()

