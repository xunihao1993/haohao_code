# -*- coding: utf-8 -*-
import multiprocessing
import time
import os

# 获取数据
def get_data(queue):
    data = queue.get()
    print('读取数据',data)

# 写入数据
def put_data(queue):
    # 拼接数据
    data = str(os.getpid())+"_"+str(time.time())
    print("压入数据:",data)
    queue.put(data)

if __name__ == '__main__':
    # 创建队列
    q = multiprocessing.Queue(3)

    # 创建5个进程用于写数据
    record1 = []
    for i in range(5):
        p = multiprocessing.Process(target=put_data,args=(q,))
        p.start()
        record1.append(p)


    # 创建5个进程用于读数据
    record2 = []
    for i in range(5):
        p =multiprocessing.Process(target = get_data,args=(q,))
        p.start()
        record2.append(p)

    for p in record1:
        p.join()

    for p in record2:
        p.join()
