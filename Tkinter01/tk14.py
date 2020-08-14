"""

Sacle

"""

from tkinter import *

root = Tk()
#   Scale也是一个滚轮（类似与游标卡尺），参数from_表示刻度从那里开始，to表示到哪里结束
#   记单词：tickinterval = tick inter val 表示显示（多么远显示一次刻度），
#   记单词：resolution = 表示移动一次的步长
s1 = Scale(root,from_=0,to=43,tickinterval=5,resolution = 5,length=200)
s1.pack()
s2 = Scale(root,from_=0,to = 200,orient=HORIZONTAL,tickinterval=10,length = 600)
s2.pack()
def show():
    print(s1.get(),s2.get())
Button(root,text="获取当前位置",command = show).pack(side= BOTTOM)


mainloop()
