"""
listbox总结：在给一个listbox添加滚轮的时候，要添加双向联系
"""
from tkinter import *

root = Tk()
#   scrollbar
s1 = Scrollbar(root)    #   Scrollbar记住单词
s1.pack(side=RIGHT,fill='y')    #   设置fill在y方向进行填充

lb = Listbox(root)  #   设置listbox
# 记住单词y（y方向的滚轮）scroll(滚轮)command(命令)
lb.config(yscrollcommand=s1.set)      # s1.set不是s1
lb.pack()
for i in range(11000):
    lb.insert(END,i)
s1.config(command=lb.yview) #   记住单词lb.yview

Button(root,text="删除这个",command=lambda x= lb: x.delete(ACTIVE))\
    .pack()


mainloop()



