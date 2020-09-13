import requests
import threading
# import re
import time


class Consumer:
    def __init__(self, all_image_url):
        super(Consumer, self).__init__()
        self.all_image_url = all_image_url
        print(all_image_url)

    def run(self):
        g_lock = threading.Lock()  # 初始化一个锁
        i = 1
        print("{}正在运行".format(threading.current_thread()))
        for url in self.all_image_url:
            # 上锁
            g_lock.acquire()
            # 得到一个url
            url = self.all_image_url.pop()
            # print(url)
            self.__download(url, i)
            i += 1
            time.sleep(5)
            # 解锁
            g_lock.release()
            # 再用正则获取图片名称

    def __download(self, url, i):
        # headers = {
        #     "User-Agent":
        #         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        #     "Referer": url
        # }
        html = requests.get(url)
        filename = "../pic/" + str(i) + url[url.rfind("."):-1]
        print(filename)
        print(url)
        # print( url[url.rfind("/"):-1])
        time.sleep(1)
        with open(filename, "wb") as f:
            f.write(html.content)


if __name__ == '__main__':
    from code.Spider import Spider
    from code.Producer import Producer

    url_ = "https://www.tupianzj.com/meinv/xiezhen/list_179_%d.html"
    sp = Spider(url_)
    sp.get_all_urls(1, 1)
    # print(sp.all_url)
    producer = Producer(sp.all_url)
    producer.run()
    # print(producer.all_image_url)
    consumer = Consumer(producer.all_image_url)
    consumer.run()
    # producer.join()
    # consumer.join()

# https://img.tupianzj.com/uploads/allimg/202003/9999/rn92f55b0242.jpg
