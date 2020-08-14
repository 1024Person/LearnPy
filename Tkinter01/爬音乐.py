# https://music.163.com/#/playlist?id=5154575129
# https://music.163.com/m/song?id=1463165983
# https://y.qq.com/n/yqq/song/004dHezI0N9LNn.html
import urllib.request


url = 'https://music.163.com/m/song?id=1463165983'

respons = urllib.request.urlopen(url)

html = respons.read()

with open('music.mp3','wb') as stream:
	stream.write(html)

print(html)
