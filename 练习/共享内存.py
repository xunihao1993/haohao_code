# -*- coding: utf-8 -*-

import multiprocessing

def run(v):
    print('子进程：',v.vlue)
    v.value += 10

if __name__ == "__main__":
    server = multiprocessing.Manager()

    v = server.Value('i',250)

    p = multiprocessing.Process(target=run,args=(v,))

    p.start()
    p.join()

    print('主进程：',v.value)

