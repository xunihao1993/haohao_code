# -*- coding: utf-8 -*-
from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self,delay):
        super().__init__()
        self.delay = delay

    def run(self):
        for i in range(3):
            print("子进程运行中....")
            time.sleep(self.delay)

if __name__ == '__main__':
    p = MyProcess(1)
    p.start()
    p.join()
    print("主进程结束")