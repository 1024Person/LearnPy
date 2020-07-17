# 字符串的内置函数  字符串类的函数成员
# about upper and lowwer
# title capitalize
message = 'zhaorui is a beautiful girl'
msg = message.capitalize()  # make frist charatcter change upper
print(msg)
msg = message.title() # make  frist charatcter of every words change upper ,and other is lower
result = msg.istitle()
print(result)
print(msg)

# change all character to upper
msg = message.upper()
print(msg.isupper(),msg)
# change all character to lower
msg = message.lower()
print(msg.islower(),msg)


s ='QWERTYUIOPLKJHGFDSAZXCVBNqwertyuioplkjhgfdsazxcvbnm0987654321'
# print(len(s))       # len ----->length return intget

import random
for i in range(0,4):
    code = ''
    for i in range(0,4):
        ran = random.randint(0,len(s) - 1)
        code += s[ran]               # string 'add' method
    print('验证码：%s'%(code)) 
    code = code.lower()               # in order to make right of both lower and upperstring  change string to lower      
    user_input = input('请输入验证码：').lower()
    if user_input == code.lower():
        print('验证码正确！')
    else:
        print('验证码错误！')