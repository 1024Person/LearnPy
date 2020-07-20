import os

path = os.path.dirname(__file__)
print(path)
result = os.path.isabs(path)
print('------------->', result)

path = os.path.abspath(__file__)
print('当前文件的绝对路径：',path)

filename = path[path.rfind('\\') + 1::]
print('文件名：', filename)

path = os.getcwd()
print('当前文件所在的文件夹：',path)

result = os.path.split(path)
print(result)

result = os.path.join(path,'file','1.txt')
print(result)
