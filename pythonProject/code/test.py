import requests

url = " https://img.tupianzj.com/uploads/allimg/202003/9999/rn92f55b0242.jpg"
filename = "../pic" + url[url.rfind("/"):]

with open(filename, 'wb') as s:
   html = requests.get(url)
   s.write(html.content)