# -*- coding: utf-8 -*-
import multiprocessing


if __name__ == '__main__':
    # 创建队列
    q = multiprocessing.Queue(3)
    # 判断队列是否为空
    print(q.empty())
    # 判断队列是否已满
    print(q.full())
    # 压入数据
    q.put('hello')
    q.put("world")
    q.put("xxx")
    # 队列已满时，在添加数据会阻塞，设置不阻塞会报错
    # q.put("yyy",False)
    # q.put("yyy")
    # 获取队列长度
    #读取数据
    print(q.get())
    print(q.get())
    print(q.get())
    # 队列为空时，读取也会阻塞
    # print(q.get())