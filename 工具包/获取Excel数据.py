# -*- coding: gbk -*-

import xlrd

def getExcelList(file_path):
    data=xlrd.open_workbook(file_path)
    table=data.sheet_by_index(0)
    nrows=table.nrows #获取行数
    ExcelList=[]
    temp_list=[]
    if nrows>1:
        for i in range(1,nrows):
            for j in range(len(table.row_values(i))):
                temp_list.append(table.row_values(i)[j].encode('gbk'))
            ExcelList.append(temp_list)
            temp_list=[]
    else:
        return ExcelList
    return ExcelList
a=getExcelList("C:\Users\haohao\Desktop\customer_201_201.xlsx")

print(a)


    
