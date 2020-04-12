# -*- coding: utf-8 -*-

from threading import Thread
import time
class MyThread(Thread):
    def __init__(self,t):
        super().__init__()
        self.t=t

    def run(self):
        for i in range(3):
            print('子线程中....')
            time.sleep(self.t)
if __name__=='__main__':
    print('主线程开始')
    p = MyThread(2)
    p.start()
    p.join()
    print("主线程结束")