# -*- coding: utf-8 -*-
import multiprocessing
import os

def copy(src,dst):
    src_fp = open(src,'r')
    dst_fp = open(dst,'w')
    content = src_fp.read(1024)
    while content:
        dst_fp.write(content)
        content = src_fp.read(1024)
    src_fp.close()
    dst_fp.close()
    print(src,'拷贝到',dst,'已完成')

if __name__ == '__main__':
    src = ''
    dst = ''
    record = []
    dirs = os.listdir(src)
    for file in dirs :
        src_file = os.path.join(src,file)
        dst_file = os.path.join(dst,file)
        #copy(src_file,dst_file)
        p=multiprocessing.Process(target = copy,args=(src_file,dst_file))
        p.start()
        record.append()
    for p in record:
        p.join()
    print("拷贝结束")