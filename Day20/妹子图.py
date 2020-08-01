import urllib.request

response = urllib.request.urlopen('https://www.baidu.bom').read()
data = response.decode('utf-8')
print(data)
