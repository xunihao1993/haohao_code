# -*- coding: utf-8 -*-
from  multiprocessing import Process
import multiprocessing
import os
import time

def aa():
    print("子进程开始")
    time.sleep(5)



def do_some_thing():
    print("子父进程开始",os.getpid())
    p = Process(target=aa)
    # p.daemon = True
    p.start()
    print("子父进程结束")


#启动子进程，会将父进程所在的文件在加载一次，没有经过处理将会五险循环下去造成错误
#因此，通常将执行的代码放到下面的结构中
# 当文件被执行的时候是无法再次执行的，当创建子线程的时候会把整个文件在启动一遍，复制一遍
if __name__ == '__main__':
    # 获取当前进程号
    do_some_thing()
    print("父进程结束")
    # print(os.getpid())
    #创建一个进程，指定任务（通过函数）
    #参数介绍：
    # target:指定任务，一个函数
    # name 进程名
    # args和kwargs:传递给子进程任务函数的参数
    # p = Process(target=do_some_thing)
    # # 获取当前进程
    # pp = multiprocessing.current_process()
    # # 当主线程结束后，子线程仍然在运行，这样的进程叫僵尸进程（有风险）
    # # 设置：当主线程结束时，结束子进程
    # p.daemon = False
    # # 启动进程
    # p.start()
    # # 等待子进程结束，在结束主线程,可以指定等待时间
    # #p.join(1)
    # # 终止子进程
    # # p.terminate()
    # print("主线程结束")
