"""

entry:输入框

"""

from tkinter import *
root = Tk()

m = Entry()
m.pack(padx = 10,pady = 10)
m.delete(0,END)
m.insert(0,"默认文本...")

mainloop()

