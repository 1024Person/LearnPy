from tkinter import *
root = Tk()
frame1 = Frame(root)
frame1.pack()
frame2 = Frame(root)
frame2.pack()
text = Text(frame1,width = 10,height = 10,undo = True)
text.pack()
photo = PhotoImage(file='12.gif')
def show():
    text.image_create(END,image = photo)    #   插入图片
text.insert(INSERT,'输入文本')
b1 = Button(frame2,text="来张图",command = show)
b1.pack(side= RIGHT)
def show():
    print(text.get("1.0",END))
b2 = Button(frame2,text="展示",command = show)
b2.pack()


# b2 = Button(frame2,text="撤销",command = )
# b2.pack()
# text.window_create(INSERT,window=b) #   插入按钮部件

mainloop()