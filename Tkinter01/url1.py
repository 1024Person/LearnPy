import urllib.request

url = 'http://www.baidu.com'

support_proxy = urllib.request.ProxyHandler({"http":"120.198.230.30:80"})


opener = urllib.request.build_opener(support_proxy)

urllib.request.install_opener(opener)

respon = urllib.request.urlopen(url)
print(respon.read().decode('utf-8'))

# print
