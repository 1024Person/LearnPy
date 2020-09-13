# 生产者对象
import threading
import requests
from code.Spider import Spider
import re
import time

url = "https://www.tupianzj.com/meinv/xiezhen/list_179_%d.html"


class Producer(threading.Thread):
    """
    继承了threading.Thread，用来当做生产者，
    分析网页代码中的图片地址，并且提取出来
    """

    def __init__(self, all_urls):
        super(Producer, self).__init__()
        self.all_image_url = []
        self.all_urls = all_urls

    def run(self):

        try:
            g_lock = threading.Lock()  # 初始化一个锁
            while len(self.all_urls) > 0:
                # 上锁，防止其他线程同时访问all_urls
                # 因为如果同时访问all_urls的话，
                # 可能会发生两个线程同时访问一个分页的情况
                # 这样的话就会发生网址保存重复
                g_lock.acquire()
                # 将这个分页的网址读取出来，防止下一个线程读取重复
                url_ = self.all_urls.pop()
                # 释放锁
                g_lock.release()
                # print("正在分析网页：{}".format(url_))
                html = requests.get(url_)  # 获取网页
                # html.content.decode("utf-8")
                # 提取图片地址
                # 这里也需要上锁，
                # 存放图片网址的时候也要将all_image_url锁住，防止存放冲突
                g_lock.acquire()
                image_src = re.findall(r'<img src="(.*?) alt=".+?" />', html.text)
                # print(image_src)
                # print(html.text)
                for img_url in image_src:
                    self.all_image_url.append(img_url)
            # 释放锁
                g_lock.release()
            time.sleep(1)  # 睡一秒
        except Exception as reason:
            print(reason)


if __name__ == '__main__':
    spider = Spider(url)
    spider.get_all_urls(1, 20)
    # for url in spider.all_url:
    #     print(url)

    producer = Producer(spider.all_url)
    producer.start()
    producer.join()

    print(producer.all_image_url)
