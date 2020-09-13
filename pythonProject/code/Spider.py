# 梦想橡皮擦的博客
# 爬取妹子图
# 获取分页地址
# 获取每个图片的地址
# 获取每一个分页的网址
import requests


class Spider:
    def __init__(self, target_url):
        self.target_url = target_url
        self.all_url = []

    def get_all_urls(self, start, end):

        for i in range(start, end + 1):
            url = self.target_url % i
            self.all_url.append(url)


if __name__ == '__main__':
    url_ = "https://www.tupianzj.com/meinv/xiezhen/list_179_%d.html"
    spider = Spider(url_)
    spider.get_all_urls(1, 26)
    for url in spider.all_url:
        html = requests.get(url=url)
        print(url)
        print(html.text)
    print(spider.all_url)
