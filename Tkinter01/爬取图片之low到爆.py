import urllib.request
from tkinter import *
import re
root = Tk()
root.title('下载"觅知网"图片')
frame1 = Frame(root)
frame2 = Frame(root)
frame1.pack()
frame2.pack()
Label(frame1,text= '输入网址：').grid(row = 0,column = 0)
def download():
	url = e1.get()
	try:
		respon = urllib.request.urlopen(url)
	except:
		e1.delete(0,END)
		return

	read = respon.read()
	#https://img.51miz.com/preview/element/00/01/12/78/E-1127890-7C01ED20.jpg!/quality/90/unsharp/true/compress/true/fw/840
	#https://img.51miz.com/preview/element/00/01/12/81/E-1128124-D1769400.jpg!/quality/90/unsharp/true/compress/true/fw/840
	#https://img-u-5.51miz.com/Element/00/84/14/48/4c7bd8d4_E841448_e331b6ff.png!/quality/90/unsharp/true/compress/true/format/png
	#https://img-u-5.51miz.com/Element/00/84/14/48/4c7bd8d4_E841448_e331b6ff.png!/quality/90/unsharp/true/compress/true/format/png
	#https://img.51miz.com/Element/00/82/63/79/67344758_E826379_030a5429.png!/quality/90/unsharp/true/compress/true/format/png/fh/630
	#https://img-u-3.51miz.com/preview/element/00/01/12/74/E-1127411-8223B85F.jpg!/quality/90/unsharp/true/compress/true/format/jpg
	#https://img.51miz.com/preview/templet/00/00/48/39/T-483910-DA59C81F.mp4
	filename = re.match(r'^.+([E e]lement)|(preview)/(.+)!.+',url)
	print(filename)
	if not filename:
		print('下载失败')
		return
	if e2.get() and e2.get()!='选填':
		filename = 'image/' + e2.get() + filename.group(1)[-4:]

	else:
		filename = filename.group(1)
		index = filename.rfind('/')
		filename = filename[index+1:]
		filename = 'image/'+filename
	print(filename)
	with open(filename,'wb') as stream:
		stream.write(read)
	e1.delete(0,END)
	e1.insert(0,'下载成功')
def dele():
	e1.delete(0,END)
e1 = Entry(frame1,width = 20)
e1.grid(row = 0,column = 1)
Label(frame1,text="重命名为：").grid(row = 1,column = 0)
e2 = Entry(frame1,width = 20)
e2.grid(row = 1,column = 1)
e2.insert(0,'选填')
e2.config(fg = 'green')
b1 = Button(frame2,text='下载',command = download).pack(side = LEFT,padx = 10 , pady = 2)
Button(frame2,text = '退出',command = root.quit).pack(side = RIGHT,padx = 10 ,pady = 2)

mainloop()