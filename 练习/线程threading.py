# -*- coding: utf-8 -*-

import threading
import time

def run(args):
    c = threading.current_thread()
    time.sleep(3)
    print('子线程开始')
    #活跃进程个数
    print(threading.active_count())
    print("子线程结束")

if __name__ == "__main__":
    # 获取主线程
    t = threading.main_thread()
    print('主线程：',t.name)
    # 获取当前线程
    # c = threading.current_thread()

    # 创建子线程
    sub = threading.Thread(target=run, args=(250,),name='下载美女图片')
    # 启动子线程
    sub.start()
    #活跃进程个数
    print(threading.active_count())
    #线程列表
    print(threading.enumerate())
    #判断线程是否活跃
    print(sub.is_alive())
    # 等待子线程
    sub.join()

    print(sub.is_alive())
    print("主线程结束："+ t.name)
