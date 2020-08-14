from tkinter import *

root = Tk()
root.title('文本编辑器')
frame1 = Frame(root)
frame2 = Frame(root)
frame1.pack()
frame2.pack()

text = Text(frame1)
text.insert(END,'插入文本')
text.pack()

text.insert(INSERT,'插入图片')
text.mark_set('here','1.2')	#	设置mark标记，名字为here	
text.insert('here','入')		#	在here处插入文本
text.insert('here','差')		#	gravity，默认是插入到here的左边每次插入都会向后移动
def dele():
	text.delete('1.0',END)
Button(frame2,text = '全部删除',command = dele).pack(side = RIGHT)
# b.grid(row = 0,column=1,padx = 10,pady = 2)
def insert():
	text.insert('here','入')		#	在here处插入文本
	text.insert('here','差')	
Button(frame2,text="插入",command = insert).pack(side = LEFT)
# b1.grid(row = 0,column = 0,padx = 10 ,pady = 2)
#	设置插入的方向
# text.mark_gravity(mark = RIGHT)


# text.mark_unset('here')		#	删除标签
# text.insert('here','入')		#	在here处插入文本,报错，
mainloop()