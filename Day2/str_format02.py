# 字符的格式化输出
# 1、使用占位符 2、format
age = 5
s = '已经上'
# format 是字符串的一个方法，‘.’是调用\
# 不指定占位的位置
message = '乔治说："我今年{}岁了",{}幼儿园'.format(age,s)
#指定顺序
message = '乔治说："我今年{0}岁了",{1}幼儿园'.format(age,s)
print(message)

name = '乔治'
age = 5
hobby = '玩恐龙'
massage = '{1}今年{0}岁了，最喜欢{2}'.format(age,name,hobby)