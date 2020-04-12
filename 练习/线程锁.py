# -*- coding: utf-8 -*-

import threading

# 这是你银行的存款
money = 250

def run(n):
    global money

    for i in range(100000):
        '''
        lock.acquire()
        try:
            # 运算之后，数据应该不变
            money = money + n
            money = money - n
        finally:
            lock.release()
        '''
        # 简化书写
        with lock:
            money = money + n
            money = money - n

if __name__ == '__main__':
    lock = threading.Lock()
    # while True:
    t1 = threading.Thread(target=run, args=(10,))
    t2 = threading.Thread(target=run, args=(15,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(money)
