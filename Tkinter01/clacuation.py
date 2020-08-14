"""
实现一个简单的计算器
"""
from tkinter import *


root = Tk()

#   v1,v2,v3与三个输出框进行绑定，
#   最后因为还要设置最后一个entry的属性为readonly
#   所以对e3的操作都被禁止了，insert也不行了
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
frame1 = Frame(root)
frame2 = Frame(root)
frame1.pack()
frame2.pack()
def test(reason):
    if reason.isdigit():
        return True
    else:
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        return False
testCMD = frame1.register(test)

def delete_x(e):
    e.delete(0,END)
deleteCMD = frame2.register(delete_x)
e1 = Entry(frame1,textvariable = v1,validate='focusout',
    vcmd=(testCMD,"%P"),width = 10)
e1.pack(side = LEFT)
l1 = Label(frame1,text='+',padx=5,pady=5,width=10)
l1.pack(side = LEFT)
e2 = Entry(frame1,textvariable = v2,validate='focusout',validatecommand=(testCMD,"%P"))
e2.pack(side = LEFT)
l2 = Label(frame1,text="=",padx=5,pady=5,width=10)
l2.pack(side = LEFT)
e3 = Entry(frame1,state='readonly',textvariable=v3)
e3.pack(side = LEFT)
def clac():
    result = int(v1.get()) + int(v2.get())
    v3.set(str(result))
Button(text='计算结果',command = clac).pack(anchor=CENTER)

mainloop()