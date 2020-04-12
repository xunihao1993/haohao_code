# -*- coding: utf-8 -*-

import os
import multiprocessing
import time

def loop(label,lock):
    #获取锁
    lock.acquire()
    time.sleep(1)
    #中间的任务，不可能同时多个进程执行
    print(label,os.getpid())
    #释放锁
    lock.release()

if __name__ == "__main__":
    print("主进程",os.getpid())
    # 创建进程锁
    lock = multiprocessing.Lock()
    # 创建多个子进程
    # 用于存储所有的进程
    recode = []
    for i in range(5):
        # p=multiprocessing.process(targe=loop,args=("子进程"))
        p = multiprocessing.Process(target=loop,args=("子进程",))
        p.start()
        recode.append(p)

    #等待进程结束
    for p in recode:
        p.join()
