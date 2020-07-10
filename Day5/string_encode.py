# 编码：中文无法在网络上进行传播，所以，需要先进行编码"encode"
# 编码之后，还要再进行解码
# message = '上课了，快学习'
# msg = message.encode('utf-8')
# print(msg)
# 
# print('-' * 30)
# result = msg.decode('utf-8')
# print(result)
# 
# --------------------
# startswith()   endswith()     返回值为布尔类型
# startswith()判读是否以xxx开头的  endswith() 判断是否以xxx结尾的 区分大小写
# 应用： 文件上传，只能上传图片(png,jpg,gif)
# file_name = '学py.py'
# result = file_name.endswith('txt')
# print(result)
# 
# path = input('请选择要上传的文件：')
# p = path.rfind(r'\')
# file_name = path[p + 1:]
# 
# if file_name.endswith('jpg') or file
#_name.endswith('png') or file_name.endswith('gif'):
    # print('{}是图片
    #，允许上传'.format(file_name))
# else:
  
  # print('{}不是图片，不允许上传'.format(file_name))
# 
# 
while True:
    path = input('请选择要上传的文件：')
    p = path.rfind('\\')            # 即使用  r 保留格式，也会报错，因为 \ 后面必须要有内容，
    file_name = path[p + 1:]
    # 
    if file_name.endswith('txt'):
      print('{}是记事本，允许上传'.format(file_name))
      break
    else:
      print('{}不是记事本，请重新上传'.format(file_name))
      