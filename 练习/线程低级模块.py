# -*- coding: utf-8 -*-

import _thread
import time
def loop():
    print("子线程开始")
    print("子线程结束")

if __name__ == '__main__':
    print("主线程开始")
    # 创建线程
    _thread.start_new_thread(loop,())
    # 主线程结束，子线程立即结束，
    time.sleep(3)
    print("主线程结束")

