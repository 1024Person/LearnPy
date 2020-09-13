import pymysql
import pymongo
import random
import threading
import re
import requests
import time

get_index = 1  # 获取连接时用到的下标
info = []  # 存储相关信息的列表
dic_list_end = []  # 最后的字典列表，用来保存所有的用户地址和索引
# all_urls = []  # 所有连接
url_pages = []  # 每一页的连接
index = 1  # 创建索引
page = 1  # 页数
db = pymongo.MongoClient().admin  # 连接数据库
g_lock = threading.Lock()


# <a href="/subscribe/chenhaoalex/5.html" class="b bC" onfocus="this.blur()">5</a>

# class SaveDB:
#     def __init__(self):
#         try:
#             self.__conn = pymysql.connect(host="localhost", user="root",
#                                           port=3306, password="1234", database="tz_db",
#                                           charset="utf8")
#             self.__cur = self.__conn.cursor()
#         except Exception as r:
#             print("连接MySQL数据库失败", r)
#         else:
#             print("连接成功")
#
#     def __str__(self):
#         return "这是一个和数据库存储有关的类"
#
#     def exec(self, sql):
#         self.__cur.execute(sql)


# 图片中里面的url用户主页连接是用户名加密之后的连接
class Config:
    def get_headers(self):
        user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]
        UserAgent = random.choice(user_agent_list)
        headers = {'User-Agent': UserAgent}
        return headers


class Producer(threading.Thread):
    def run(self):
        global dic_list_end
        global page
        global index

        print("线程启动……")
        headers = Config().get_headers()
        html = requests.get(url="http://www.moko.cc/subscribe/chenhaoalex/1.html",
                            headers=headers)
        content = html.text
        #  获取页面的数量
        pages = re.findall(r'<a href=\"/.*?\" class=".*?" onfocus=\"this\.blur\(\)\">(\d*?)</a>'
                           , content, re.S)
        print(pages)
        if len(pages) <= 0:
            exit(0)
        size = int(max(pages))  # 获取最大的页面数量
        url = "http://www.moko.cc/subscribe/chenhaoalex/%d.html"
        while page <= size:  # 这里用page也是为了多线程之间的通信
            g_lock.acquire()  # 上锁
            dic = {'index': page, "url": url % page}
            url_pages.append(dic)  # 获取每一页的连接地址
            page += 1
            g_lock.release()  # 解锁
        # print(url_pages)
        while True:
            g_lock.acquire()  # 上锁
            if len(url_pages) <= 0:
                g_lock.release()  # 释放锁
                time.sleep(0.2)  # 将CPU的使用权转移出去
            else:
                url = url_pages.pop()
                # print(url)
                g_lock.release()  # 释放锁
                html = requests.get(url=url["url"], headers=headers)  # 请求当前网页
                content = html.text
                url_list = re.findall(
                    r'<a class=\"imgBorder\" href=\"/(.*?)\" hidefocus=\"true\">',
                    content)  # 临时的url，也是陈小刀关注的每一个用户的url
                while len(url_list) > 0:
                    u = url_list.pop()
                    pattern = re.compile(r"chenhaoalex")
                    temp_url = pattern.sub(u, url['url'])  # 获取每一页的中所有用户的url
                    # all_urls.append(temp_url)  # 将所有用户的url保存起来
                    g_lock.acquire()
                    dic = {"index": index, "url": temp_url}
                    dic_list_end.append(dic)
                    index += 1  # 将当前索引加一
                    db.admin.insert_one(dic)
                    g_lock.release()
                # 为什么不能直接一起将所有的数据都插入到数据库中？
                # 感觉可能是数据重复了
                # try:
                #     db.admin.insert_many(dic_list_end, ordered=False)  # 将所有的数据保存到数据库中
                # except Exception as r:
                #     print("插入数据失败")
                #     print(r)
                #     exit(0)


class Consumer(threading.Thread):
    def run(self):
        """
        消费者的作用就是从mongodb数据库中读取到所有的url
        然后将得到的url的主页信息读取下来
        :return:
        """
        # 下面的就是要爬取的结构，先分析一下，首先这是一个div标签，其次div标签里面套着两个标签，
        # 一个标签中有用的信息就是url头像<img>
        # 另一个有用的信息就是用户信息之类的
        #     <div class="info cf">
        # 	    <img class="icon bd" src="http://img.mb.moko.cc/2018-04-06/4e05b28d-8d7d-46cf-9cdf-c2acbb946fc7.jpg" title="佟钰滢" alt="佟钰滢">
        # 	    <p class="gC" style="float:left;">5岁<span>&nbsp;北京</span><br><a class="gmC u" href="http://html.moko.cc/html/astro/Taurus.html" target="_blank" title="">金牛座</a><br>2美分&nbsp;&nbsp;V1级别</p>
        # </div>
        # 指定正则表达式

        #  获取网页内容
        global get_index
        headers = Config().get_headers()

        while True:
            g_lock.acquire()  # 上锁
            #  先从数据库中读取出来所有的网址
            dic_url = db.admin.find_one_and_delete({"index": get_index})
            print(dic_url)
            get_index += 1
            g_lock.release()  # 解锁
            html = requests.get(url=dic_url["url"], headers=headers)
            content = html.text
            pattern = re.compile(
                r'<img class=\".*?\" src=\"(.*?)\" title=\"(.*?)\" alt=\".*?\">'
                r'<p class=\".*?\"> style=\".*?\">(\d*?)岁<span>&nbsp;(.*?)'
                r'</span><br><a class=\".*?\" href=\".*?\" target=\".*?\" .*?>(.*?)'
                r'</a><br>(\d*?)美分&nbsp;&nbsp;(.*?)级别</p>')
            us_in = pattern.findall(content)
            print(us_in)


if __name__ == '__main__':
    # 开五个线程
    for i in range(5):
        producer = Producer()
        producer.start()
    for i in range(5):
        consumer = Consumer()
        consumer.start()
