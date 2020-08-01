#   加密算法的库
#   加密算法有可以解密的，也有不可逆的
import hashlib


msg = ' 中午一起吃饭去'
md5 = hashlib.md5(msg.encode('utf-8'))  # 加密，md5不接受汉字，只能将md5进行编码，传递给md5
print(md5.hexdigest())

sha256 = hashlib.sha256(msg.encode('utf-8'))
print(sha256.hexdigest())

password = '123456'
