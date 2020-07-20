# try  except  finally
# except 可以有很多个
# error 有很多的种类，在小甲鱼论坛上有整理这个文档

def func(number):
    try:
        a = number
        b = 1
        print(b / a)
        with open('111.txt') as stream:
            print(stream.read())
    except ZeroDivisionError:   # 除数为零的异常
        print('除数不能为零')
    except Exception as err:    # 全部的异常 加上 as是因为的意思
        print('出错了', err)
    finally:
        stream.close()


func(1)
