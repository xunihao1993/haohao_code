# -*- coding: utf-8 -*-
import multiprocessing

def run(p_a):
    # 子进程给主进程发数据
    # p_a.send(['a','b','c'])
    recv=p_a.recv()
    print('子进程接收到',recv)

if __name__ == '__main__':
    # 创建管道，默认是全双工的，两边都可以收发
    # duplex=False,是半双工，p_a只能收，p_b只能发
    p_a,p_b = multiprocessing.Pipe(duplex=False)
    p = multiprocessing.Process(target=run,args=(p_a,))
    p.start()
    # 主进程向子进程发数据
    p_b.send([1,2,3,4,5])
    p.join()
    # print("主进程收到：",p_b.recv())
    print("主进程结束")