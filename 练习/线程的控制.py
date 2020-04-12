# -*- coding: utf-8 -*-
import threading
import time
def run(num):
    print(aa)
    for i in range(num):
        # 等待条件成立,会阻塞
        e.wait()
        print('第%d步'%(i+1))
        #清除条件
        e.clear()
if __name__=="__main__":
    aa='1'
    e = threading.Event()
    threading.Thread(target = run,args=(3,)).start()
    for i in range(3):
            time.sleep(1)
            # 设置后， wait处将不再阻塞
            e.set()
            print('走你',end='')