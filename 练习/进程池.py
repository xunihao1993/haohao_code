# -*- coding: utf-8 -*-

import multiprocessing
import time
import random

#进程函数结束后会回调，参数时进程函数的返回值
def callback(s):
    print(s,"结束")

# 进程任务
def task(num):
    print("开始")
    start = time.time()
    time.sleep(random.random()*5)
    end = time.time()
    print(num,"执行了:",(end-start))
    return num

if __name__== '__main__':
    # 获取CPU核心数
    print('核心',multiprocessing.cpu_count())
    # 创建进程池,一般进程池中的进程数不超过CPU核心数
    pool = multiprocessing.Pool(4)
    # 循环创建进程并添加到进程池中
    for i in range(5):
        # 参数：
        # func:任务函数
        # args:任务函数的参数
        # callback:回调函数，进程结束时调用，参数时进程函数的返回值
        pool.apply_async(func=task,args=(i,),callback=callback)
    #关闭进程池，关闭后就不能再添加进程了
    pool.close()
    #等待进程池
    pool.join()
    print("主进程结束")
