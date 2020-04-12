# -*- coding: utf-8 -*-
import threading
import os
def run():
    print('aaa')
    os.system('start Notepad++')

if __name__ == '__main__':
    t=threading.Timer(3,run)
    t.start()
    t.join()
