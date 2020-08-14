import urllib.request
import urllib.parse
url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
data = {}

data['from'] = 'zh'
data['to'] = 'en'

data['transtype'] = 'translang'
data['simple_means_flag'] = '3'
data['sign'] = '47194.285547'
data['token'] = '20e884d9e010e0a3159e4acacfb046be'
data['domain'] = 'common'

data['query'] = '我爱你'
data = urllib.parse.urlencode(data).encode('utf-8')


respon = urllib.request.urlopen(url,data)
# print(respon.read().decode())

html = respon.read().decode('utf-8')
# print(html["query"])
print(html)
