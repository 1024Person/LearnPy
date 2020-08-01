class Singleton:
    __instance = None  # 存放地址

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)  # 接收地址，将地址返回出去
            return cls.__instance
        else:
            return cls.__instance  # 如果地址已经存在了，将地址返回出去


s = Singleton()
s1 = Singleton()
s2 = Singleton()
s3 = Singleton()
print(s)
print(s1)
print(s2)
print(s3)
