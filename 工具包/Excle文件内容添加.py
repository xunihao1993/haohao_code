# -*- coding: gbk -*-

############################Excle内容添加##############################
import xlrd
from xlutils.copy import copy
from xlwt import Style
import xlwt
import os



def writeExcel(__REQ__,file_path):
	#__REQ__：数据元组或列表
    #file_path：文件路径


    #file_path = unicode(file_path,"utf-8") #中文路径
    
    #判断文件是否存在 若存在获取文件大小 若不存在赋文件大小为0
    if os.path.exists(file_path):
        fsize = os.path.getsize(file_path) #获取文件大小 
    else:
        fsize=0 #文件大小赋0
    if fsize == 0:
        files = xlwt.Workbook()
        table = files.add_sheet('info',cell_overwrite_ok=True)
        for i in range(0,len(__REQ__)):
            table.write(0,i,__REQ__[i].decode("gbk"))
        files.save(file_path)
    else:
        style = xlwt.easyxf('');#添加样式
        rb = xlrd.open_workbook(file_path,formatting_info=True)
        table = rb.sheet_by_index(0)#通过索引顺序获取
        norows = table.nrows #获取原文件的行数
        wb = copy(rb)
        ws = wb.get_sheet(0)
        for i in range(0,len(__REQ__)):
            ws.write(norows,i,__REQ__[i].decode("gbk"),style)
            wb.save(file_path)



files="C:\Users\haohao\Desktop\customer_201_113031.xls"
list=('C12136', '01 是', '', '', '01 境内', '', '01 新增', '', '2017120709271299133', '01 普通个人', '00 居民身份证', '', '', '460102198902042710', '', '', '', '武大', '02 女', '04 成长型', '17789880204', '无', '66402214@qq.com', '', '2017120711842294')
list1=("浩浩333",'1','2')
writeExcel(list,files)
writeExcel(list1,files)
