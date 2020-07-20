# with open(r'C:\Users\ASUS\Desktop\usually_using\Learn_Py\Day13\Node\GitHub.jpg ','rb') as jpg:
#     jpg.readlines()
#     print(jpg.readlines())

import os

path = os.path.dirname(__file__)
path1 = os.path.join(path, 'GitHub.jpg')
path2 = os.path.join(path, 'git.jpg')   #注意：这里的文件名字好像对 大小写不敏感，也就是说大写的A和a是一样的
with open(path1, 'rb') as stream:
    container = stream.read()
    with open(path2, 'wb') as wstream:
        wstream.write(container)
        print(path2)

print('文件复制完成')


