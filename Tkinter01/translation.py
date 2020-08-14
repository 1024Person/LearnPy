import urllib.request
import urllib.parse
import json
from tkinter import *



root = Tk()

v = StringVar()
root.title('某道翻译')
Label(root,text = '请输入你要翻译的内容：')\
	.grid(row = 0,column = 0,padx = 5 ,pady = 2)

t1 = Text(root)
t1.grid(row = 1,column = 0)
Label(root,text = '翻译结果为：')\
	.grid(row = 0,column = 1,padx = 5 ,pady = 2)
photo = PhotoImage(file ="image/水火二极.png")
Label(root,textvariable=v,image = photo,compound = CENTER,font = ('楷体')).\
	grid(row = 1,column = 1,padx = 5,pady = 2)

def translation():

	url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
	data = {}
	data['i'] = t1.get('1.0',END)

	
	data['from']= 'AUTO'
	data['to']  = 'AUTO'
	data['smartresult'] ='dict'
	data['client'] ='fanyideskweb'
	data['salt'] = '15964406088667'
	data['sign'] = '8722a85cc1f6c23ecc581b91a8fe116e'
	data['ts'] = '1596440608866'
	data['bv'] = '7b07590bbf1761eedb1ff6dbfac3c1f0'
	data['doctype'] = 'json'
	data['version'] = '2.1'
	data['keyfrom'] = 'fanyi.web'
	data['action'] = 'FY_BY_CLICKBUTTION'

	data = urllib.parse.urlencode(data).encode('utf-8')


	respon = urllib.request.urlopen(url,data)
	
	html = respon.read().decode('utf-8')
	# print(html["translateResult"][0][0]["tgt"])

	# print(type(html))
	html = json.loads(html)

	try:
		print(html['translateResult'][0][0]['tgt'])
	
	except KeyError:
		v.set('')
		return
	
	# t2.delete('0.0',END)
	# t2.image_create("insert",image = photo)
	# print(html)

	result = ''
	for res1 in html['translateResult']:
		for res2 in res1:
			result+=res2['tgt']+'\n'
	
	v.set(result)
Button(root,text='翻译',width = 10,activebackground = 'green',command=translation).\
	grid(row = 2,column = 0,padx = 5,pady = 2)
Button(root,text = '退出',width = 10 ,command = root.quit).\
	grid(row = 2,column = 1,padx = 5,pady = 2)


mainloop()