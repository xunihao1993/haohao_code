# -*- coding: gbk -*-

'''
����ʹ��xlsx��ʽ
xls��ʽ���ܻᱨ��
'''
from faulthandler import dump_traceback
import xlrd
from xlutils.copy import copy
from xlwt import Style
import xlwt
import os
import traceback
import re

#��ȡexcel�������
def getExcelList(file_path):
    data=xlrd.open_workbook(file_path)
    table=data.sheet_by_index(0)
    nrows=table.nrows #��ȡ����
    print(nrows)
    ExcelList=[]
    temp_list=[]
    if nrows>1:
        for i in range(0,nrows):
            for j in range(len(table.row_values(i))):
                temp_list.append(str(table.row_values(i)[j]))
            ExcelList.append(temp_list)
            temp_list=[]
    else:
        return ExcelList
    return ExcelList

#׷��excep����
def writeExcel(__REQ__, file_path):
    # __REQ__������Ԫ����б�
    # file_path���ļ�·��

    # file_path = unicode(file_path,"utf-8") #����·��

    # �ж��ļ��Ƿ���� �����ڻ�ȡ�ļ���С �������ڸ��ļ���СΪ0
    if os.path.exists(file_path):
        fsize = os.path.getsize(file_path)  # ��ȡ�ļ���С
    else:
        fsize = 0  # �ļ���С��0
    if fsize == 0:
        files = xlwt.Workbook()
        table = files.add_sheet('info', cell_overwrite_ok=True)
        for i in range(0, len(__REQ__)):
            table.write(0, i, __REQ__[i])
        files.save(file_path)
    else:
        style = xlwt.easyxf('');  # �����ʽ
        rb = xlrd.open_workbook(file_path, formatting_info=True)
        table = rb.sheet_by_index(0)  # ͨ������˳���ȡ
        norows = table.nrows  # ��ȡԭ�ļ�������
        wb = copy(rb)
        ws = wb.get_sheet(0)
        for i in range(0, len(__REQ__)):
            ws.write(norows, i, __REQ__[i], style)
            wb.save(file_path)
#��ȡ�б���Ϣ
def extract_list(ori_data_list,num_list):
    data_list = [];
    temp_list = []
    for i in range(len(ori_data_list)):
        for j in num_list:
            temp_list.append(ori_data_list[i][j])
        data_list.append(temp_list)
        temp_list = []
    return data_list
def main():
    try:
        data_file=input('�����������ļ�����')
        compare_file=input('����������ļ�����')
        result_file='jieguo.xls'
        ori_data=getExcelList(data_file)[1:-1]#��ȡ�����ļ�����
        compare_data=getExcelList(compare_file)#��ȡ�����ļ�����
        print('ԭ�ļ�������'+str(len(ori_data)))
        print('�Ƚ��ļ�������' + str(len(compare_data)))
        # ��ȡ�б���Ϣ   �Ա���/����(1)��Ʒ����(2)����(7)���ۼ�(8)ë����%(31)
        ori_data = extract_list(ori_data, [1,2,7,8,31])
        #������б��������ַ���
        for i in range(len(compare_data)):
            compare_data[i][0]=compare_data[i][0].replace(".0","")
        #д��Excel����
        writeExcel(['��������','��������','��Ʒ����','������Ӧ��','ԭ���ۼ�',
                    'ԭ������','�ֽ�����','ë����','�������Ƿ񲨶�','�۸��Ƿ�','�쳣ԭ��'],result_file)
        #�б����
        result_list=[];
        parttern1=re.compile(r'^[0-9]*?$');
        num_bak = 0;
        num_stock = 0;
        for i in range(len(compare_data)):
            num = 0;
            result_list_temp = ['','','','','','','','','','',''];
            temp = []
            print('��ʼƥ���%s������'%i)
            if parttern1.search(compare_data[i][0]):
                num_stock = num_stock + 1;
                #print(ori_data)
                for j in range(len(ori_data)):
                    # print('�ڶ���ѭ������'+str(len(ori_data)))
                    # print('��'+str(i)+'�δ�ѭ������'+str(j)+'��Сѭ��')
                    # print('ԭ�����ļ���ȡ�����룺'+ori_data[j][0][-len(compare_data[i][0]):])
                    # print('�Ƚ��ļ����룺' + compare_data[i][0])
                    #������ƥ��
                    if ori_data[j][0][-len(compare_data[i][0]):]==compare_data[i][0]:
                        temp=ori_data[j];
                        num=num+1;
            else:
                supplier_name=compare_data[i][0];
                print(supplier_name)
                continue
            if num==1:
                print('������ƥ��ɹ�')
                result_list_temp[0]=compare_data[i][0];   #��������
                result_list_temp[1] =temp[0];  #��������
                result_list_temp[2] =temp[1];  #��Ʒ����
                result_list_temp[3] =supplier_name;  #������Ӧ��
                result_list_temp[4] =temp[3];  #ԭ���ۼ�
                result_list_temp[5] =temp[2];  #ԭ������
                result_list_temp[6] =compare_data[i][1];  #�ֽ�����
                result_list_temp[7] =temp[4];  #ë����
                result_list_temp[10] ='��';  #�쳣ԭ��

                if float(result_list_temp[6])==float(result_list_temp[5]):
                    result_list_temp[8] = '��';  # �������Ƿ��в���
                    result_list_temp[9] ='0';  # �۸��Ƿ�
                else:
                    result_list_temp[8] = '��';  # �������Ƿ��в���
                    result_list_temp[9] =str(round(float(result_list_temp[6])-float(result_list_temp[5]),2)); # �۸��Ƿ�
            else:
                print('������ƥ��ʧ��')
                result_list_temp[0]=compare_data[i][0];#��������
                result_list_temp[3] =supplier_name;  #������Ӧ��
                result_list_temp[8] ="��";  #�������Ƿ��в���
                if num==0:
                    result_list_temp[10] = "����ƥ�䲻��";  # �쳣ԭ��
                if num>1:
                    result_list_temp[10] = "���ڶ������";  # �쳣ԭ��
            writeExcel(result_list_temp, result_file)
            num_bak=num_bak+1
        writeExcel(['�������ܸ���Ϊ',str(num_stock)], result_file)
        writeExcel(['д���������Ϊ',str(num_bak)], result_file)

    except FileNotFoundError:
        print('�ļ�������')
        exp=traceback.format_exc()#��ȡ�쳣��Ϣ
        #print(exp)

if __name__=='__main__':
    main()
    print('�ļ��Ա����')





