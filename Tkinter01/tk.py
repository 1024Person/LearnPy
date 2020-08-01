#!/usr/bin/python

from tkinter import *

tk = Tk()

w = Canvas(tk,bg='white')


def printf():
    print('hekk')


b = Button(tk, text="点我", bg='white', command=printf, activebackground="green", activeforeground="black", bd=20,
           font='楷体',
           relief='flat')
b.pack()
text = Entry(xscrollcommand=False)
print(text.get())
text.pack()

w.create_rectangle(10, 10, 200, 200, fill='black')
w.pack()

tk.mainloop()
