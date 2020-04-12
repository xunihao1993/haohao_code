# -*- coding: utf-8 -*-
import threading

#全局变量

num=250

def thread_one():
    global num
    num +=10
def thread_two():
    global num
    num -=100

if __name__=="__main__":
    print("主线程", num)
    t1 = threading.Thread(target=thread_one)
    t1.start()
    t1.join()
    print("主线程",num)
    t2 = threading.Thread(target=thread_two)
    t2.start()
    t2.join()
    print("主线程", num)
