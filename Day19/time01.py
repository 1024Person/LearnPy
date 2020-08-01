import time

t = time.time()

s = time.ctime(t)
print(s)
r = time.localtime(t)
print(r.tm_mday)
 
t = time.strftime('%Y-%m-%d  %H-%M-%S')
print(t)

