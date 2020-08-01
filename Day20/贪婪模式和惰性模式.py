#   在python中默认是贪婪模式的
#   例如下面
# import re
#
# msg = 'abc123abc'
# result = re.match(r'abc\d+', msg)
# print(result)  # 匹配结果为abc123，但是abc1就是已经符合条件的字符串了，但是由于是贪婪模式，总是匹配多的字符串，所以就会匹配完
#
# result = re.match(r'abc\d+?', msg)
# print(result)  # 匹配结果为 abc1
#


#   爬图片，一点都不会就是照着抄网上的

import re
import requests

#   https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1616275527,2752836766&fm=26&gp=0.jpg
#   https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1616275527,2752836766&amp;fm=26&amp;gp=0.jpg
path = '<img class="main_img img-hover" data-imgurl="https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1616275527,2752836766&amp;fm=26&amp;gp=0.jpg" src="https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1616275527,2752836766&amp;fm=26&amp;gp=0.jpg" style="background-color: rgb(219, 191, 178); width: 123px; height: 178px; --darkreader-inline-bgcolor:#342e25;" data-darkreader-inline-bgcolor="">'

result = re.match(
    r'<img class="main_img img-hover" data-imgurl="https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1616275527,2752836766&amp;fm=26&amp;gp=0.jpg" src="(.+)amp;(.+)amp;(.+?)"',
    path)
result = result.group(1) + result.group(2) + result.group(3)
r = requests.get(result)
with open('bb.jpg', 'wb') as wstream:
    wstream.write(r.content)
