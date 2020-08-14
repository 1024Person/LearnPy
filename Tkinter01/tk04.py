from tkinter import *

root = Tk()
image = PhotoImage(file = "13.png")
imagelabel = Label(root,image=image)
#   设置背景图片的方法，用label标签，提前准备一个image对象，
#   将image对象传递给label标签中，设置compound为CENTER
#   将文本打印在图片的中间 
thelabel=Label(root,text="学py\n从入门到放弃",
    justify=LEFT,
    image=image,
    compound=CENTER,
    font=("楷体",20),
    fg='red')
thelabel.pack(side=LEFT)
root.mainloop()




