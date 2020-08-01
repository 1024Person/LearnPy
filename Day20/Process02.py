"""
进程之间的通信
通过一个公共的变量，进行传参传递

"""

from multiprocessing import Process
from multiprocessing import Queue
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


#   怎么没有了那种回收了？
if __name__ == '__main__':
    musics = Queue(3)
    p1 = Process(target=download, args=(musics,))
    p1.start()
    p2 = Process(target=listen_music, args=(musics,))
    p2.start()
    # p1.join()
    # p2.join()
    # p1.close()
    # p2.close()
