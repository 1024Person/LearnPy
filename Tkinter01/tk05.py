from tkinter import *

def callback():
    global var
    var.set("哈哈，骗你的")

root = Tk() # 创建主窗口

frame1 = Frame(root)    #   框架1   上面的字体和图片
frame2 = Frame(root)    #   框架2   下面的按钮
photo = PhotoImage(file = "12.gif")
imagelabel = Label(frame1,image=photo)
var = StringVar()   #tk中的专用字符串StringVar
var.set("点击下面阅读全文开始观看") #set方法
textlabel = Label(frame1,
    textvariable=var,
    )
textlabel.pack(padx=10)

imagelabel.pack(side = RIGHT)
button = Button(frame2,
    text="阅读全文",
    justify=LEFT,
    command=callback)


button.pack(side=BOTTOM)
frame1.pack(padx=10,pady=10)
frame2.pack(padx=10,pady=10)

root.mainloop()

# textLable = Label(root,
# text="vsc怎么闲着没事又报错？",
# font=("楷体",20),
# bg="black",
# fg="white")
# textLable.pack(side=LEFT,padx=10,pady=10)
# photo = PhotoImage(file="12.gif")
# imagelabel = Label(root,image=photo)
# imagelabel.pack(side=RIGHT)

