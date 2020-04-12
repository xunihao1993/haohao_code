# -*- coding: gbk -*-

'''
尽量使用xlsx格式
xls格式可能会报错
'''
from faulthandler import dump_traceback
import xlrd
from xlutils.copy import copy
from xlwt import Style
import xlwt
import os
import traceback
import re

#获取excel表格数据
def getExcelList(file_path):
    data=xlrd.open_workbook(file_path)
    table=data.sheet_by_index(0)
    nrows=table.nrows #获取行数
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

#追加excep内容
def writeExcel(__REQ__, file_path):
    # __REQ__：数据元组或列表
    # file_path：文件路径

    # file_path = unicode(file_path,"utf-8") #中文路径

    # 判断文件是否存在 若存在获取文件大小 若不存在赋文件大小为0
    if os.path.exists(file_path):
        fsize = os.path.getsize(file_path)  # 获取文件大小
    else:
        fsize = 0  # 文件大小赋0
    if fsize == 0:
        files = xlwt.Workbook()
        table = files.add_sheet('info', cell_overwrite_ok=True)
        for i in range(0, len(__REQ__)):
            table.write(0, i, __REQ__[i])
        files.save(file_path)
    else:
        style = xlwt.easyxf('');  # 添加样式
        rb = xlrd.open_workbook(file_path, formatting_info=True)
        table = rb.sheet_by_index(0)  # 通过索引顺序获取
        norows = table.nrows  # 获取原文件的行数
        wb = copy(rb)
        ws = wb.get_sheet(0)
        for i in range(0, len(__REQ__)):
            ws.write(norows, i, __REQ__[i], style)
            wb.save(file_path)
#提取列表信息
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
        data_file=input('请输入数据文件名：')
        compare_file=input('请输入进货文件名：')
        result_file='jieguo.xls'
        ori_data=getExcelList(data_file)[1:-1]#获取数据文件内容
        compare_data=getExcelList(compare_file)#获取进货文件内容
        print('原文件个数：'+str(len(ori_data)))
        print('比较文件个数：' + str(len(compare_data)))
        # 提取列表信息   自编码/条码(1)商品名称(2)进价(7)零售价(8)毛利率%(31)
        ori_data = extract_list(ori_data, [1,2,7,8,31])
        #处理掉列表中冗余字符串
        for i in range(len(compare_data)):
            compare_data[i][0]=compare_data[i][0].replace(".0","")
        #写入Excel内容
        writeExcel(['条件条码','完整条码','商品名称','进货供应商','原零售价',
                    '原进货价','现进货价','毛利率','进货价是否波动','价格涨幅','异常原因'],result_file)
        #列表查找
        result_list=[];
        parttern1=re.compile(r'^[0-9]*?$');
        num_bak = 0;
        num_stock = 0;
        for i in range(len(compare_data)):
            num = 0;
            result_list_temp = ['','','','','','','','','','',''];
            temp = []
            print('开始匹配第%s个条码'%i)
            if parttern1.search(compare_data[i][0]):
                num_stock = num_stock + 1;
                #print(ori_data)
                for j in range(len(ori_data)):
                    # print('第二次循环次数'+str(len(ori_data)))
                    # print('第'+str(i)+'次大循环，第'+str(j)+'次小循环')
                    # print('原数据文件截取后条码：'+ori_data[j][0][-len(compare_data[i][0]):])
                    # print('比较文件条码：' + compare_data[i][0])
                    #条形码匹配
                    if ori_data[j][0][-len(compare_data[i][0]):]==compare_data[i][0]:
                        temp=ori_data[j];
                        num=num+1;
            else:
                supplier_name=compare_data[i][0];
                print(supplier_name)
                continue
            if num==1:
                print('条形码匹配成功')
                result_list_temp[0]=compare_data[i][0];   #条件条码
                result_list_temp[1] =temp[0];  #完整条码
                result_list_temp[2] =temp[1];  #商品名称
                result_list_temp[3] =supplier_name;  #进货供应商
                result_list_temp[4] =temp[3];  #原零售价
                result_list_temp[5] =temp[2];  #原进货价
                result_list_temp[6] =compare_data[i][1];  #现进货价
                result_list_temp[7] =temp[4];  #毛利率
                result_list_temp[10] ='无';  #异常原因

                if float(result_list_temp[6])==float(result_list_temp[5]):
                    result_list_temp[8] = '无';  # 进货价是否有波动
                    result_list_temp[9] ='0';  # 价格涨幅
                else:
                    result_list_temp[8] = '有';  # 进货价是否有波动
                    result_list_temp[9] =str(round(float(result_list_temp[6])-float(result_list_temp[5]),2)); # 价格涨幅
            else:
                print('条形码匹配失败')
                result_list_temp[0]=compare_data[i][0];#条件条码
                result_list_temp[3] =supplier_name;  #进货供应商
                result_list_temp[8] ="有";  #进货价是否有波动
                if num==0:
                    result_list_temp[10] = "条码匹配不到";  # 异常原因
                if num>1:
                    result_list_temp[10] = "存在多个条码";  # 异常原因
            writeExcel(result_list_temp, result_file)
            num_bak=num_bak+1
        writeExcel(['进货单总个数为',str(num_stock)], result_file)
        writeExcel(['写入条码个数为',str(num_bak)], result_file)

    except FileNotFoundError:
        print('文件不存在')
        exp=traceback.format_exc()#获取异常信息
        #print(exp)

if __name__=='__main__':
    main()
    print('文件对比完成')





