"""

线程和进程
进程占据的cpu资源很多，一般不用于下载，只是在进程中开几个线程进行下载
进程：process
线程：threading
"""
import threading
from queue import Queue
from time import sleep


def download(musics):
    music_ = ['芒种', '画皮', '我爱你']
    for music in music_:
        sleep(0.5)
        musics.put(music)
        print('正在下载{}'.format(music))


def listen_music(musics):
    while True:
        try:
            sleep(1)
            music = musics.get(timeout=2)
            print('{}正在保存'.format(music))
        except:
            print('全部保存成功！')
            break


if __name__ == '__main__':
    music = Queue(3)
    threading1 = threading.Thread(target=download, args=(music,))
    threading2 = threading.Thread(target=listen_music, args=(music,))
    threading1.start()
    threading2.start()
