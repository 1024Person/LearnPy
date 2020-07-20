stream = open(r'C:\Users\ASUS\Desktop\usually_using\Learn_Py\Day13\Node\1.txt', encoding='UTF-8')

# container = stream.read()
# print(container)

result = stream.readable()
print(result)
while True:
    line = stream.readline()    #读取一行
    print(line)
    if not line:
        break
stream.seek(0,0)
lines = stream.readlines()
print(lines)
