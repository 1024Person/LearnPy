def register():
    username = input('输入用户名')
    if len(username) < 6:
        raise Exception('用户名必须在六位以上')


try:
    register()
except Exception as err:
    print('登录失败')
    print(err)
else:  # 如果没有接到异常就会进入else
    print('登录成功')
finally:  # 无论是否有异常都会进入finally代码块
    print('**' * 40)

# 如果发生了异常，就会向上抛如果没有能接住的就会抛出到控制台

# 扔异常分为系统自己仍异常，和自己手动扔异常
