# -*- coding: gbk -*-

############################Excle�������##############################
import xlrd
from xlutils.copy import copy
from xlwt import Style
import xlwt
import os



def writeExcel(__REQ__,file_path):
	#__REQ__������Ԫ����б�
    #file_path���ļ�·��


    #file_path = unicode(file_path,"utf-8") #����·��
    
    #�ж��ļ��Ƿ���� �����ڻ�ȡ�ļ���С �������ڸ��ļ���СΪ0
    if os.path.exists(file_path):
        fsize = os.path.getsize(file_path) #��ȡ�ļ���С 
    else:
        fsize=0 #�ļ���С��0
    if fsize == 0:
        files = xlwt.Workbook()
        table = files.add_sheet('info',cell_overwrite_ok=True)
        for i in range(0,len(__REQ__)):
            table.write(0,i,__REQ__[i].decode("gbk"))
        files.save(file_path)
    else:
        style = xlwt.easyxf('');#�����ʽ
        rb = xlrd.open_workbook(file_path,formatting_info=True)
        table = rb.sheet_by_index(0)#ͨ������˳���ȡ
        norows = table.nrows #��ȡԭ�ļ�������
        wb = copy(rb)
        ws = wb.get_sheet(0)
        for i in range(0,len(__REQ__)):
            ws.write(norows,i,__REQ__[i].decode("gbk"),style)
            wb.save(file_path)



files="C:\Users\haohao\Desktop\customer_201_113031.xls"
list=('C12136', '01 ��', '', '', '01 ����', '', '01 ����', '', '2017120709271299133', '01 ��ͨ����', '00 �������֤', '', '', '460102198902042710', '', '', '', '���', '02 Ů', '04 �ɳ���', '17789880204', '��', '66402214@qq.com', '', '2017120711842294')
list1=("�ƺ�333",'1','2')
writeExcel(list,files)
writeExcel(list1,files)
