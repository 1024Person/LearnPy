st1 = 'asd45'
print(st1.isalpha())   # 判断是否是字母（字符串是否全部是字母）
print(st1.isdigit())   # 判断是否全是数字

# isdigit 在强转数字的时候，用到提前判断一下，是否可以转换，如果不是数字的话，强转就会报错

#sum = 0
#count = 3
#for i in range(count):
#    num = input('请输入：')
#    if num.isdigit():
#        sum += int(num)
#    else:
#        pass
#print(sum)

#sum = 0
#·i = 1
#while i <= 3:
#    num = input('输入数字:')
#    if num.isdigit():
#        num = int(num)
#
#        sum += num
#    else:
#        print(num+'不是数字')
#        i-=1
#    i+=1
#print(sum)
#
# join(seq) 加入 将一些零散的字符串接起来

# new_str = '/'.join(['2020','07','09'])
# print(new_str)

list1 = ['a','b','c','d','c           ']
new_str = '-'.join(list1)   # join 指定拼接字符的链接字符
print(new_str)
s = new_str.rstrip()        # lstrip将左侧的空格去掉，返回去掉之后的字符串，但是源字符串的内容不变
print(s)
new_str = '            '+new_str
print(new_str)
print(new_str.lstrip())
new_str = 'hello world ,I must learn well English'
print(new_str.split(' ',2))      # 切割，将第一个第一个参数作为分隔符进行切割，第二格参数就是切几刀
print(new_str.count(' '))       # 查找某一个字符在字符串中出现的次数