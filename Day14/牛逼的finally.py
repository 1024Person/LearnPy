def func(number):
    try:
        return 1 / number
    except ZeroDivisionError:
        print('除数不能为零')
    except Exception as err:
        print(err)
    finally:
        return number


number = 10
number = func(number)
print(number)
# 当最后又finally的时候return也不管用，最后还是返回finally
#  中返回的值
