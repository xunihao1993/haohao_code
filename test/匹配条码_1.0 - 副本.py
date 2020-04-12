# -*- coding: gbk -*-

'''
尽量使用xlsx格式
xls格式可能会报错
最后修订时间2019-4-16  20：23
'''
from faulthandler import dump_traceback
import xlrd
from xlutils.copy import copy
from xlwt import Style
import xlwt
import os
import traceback
import re
from datetime import datetime


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
#字典初始化
def dict_init(list1,list2):
    temp = {};
    if len(list1)==len(list2):
        for i in range(len(list1)):
            if type(list1[i]).__name__=='str':
                temp[list1[i]]=list2[i]
            else:
                print('字典非法参数：键类型非法')
                return None
    else:
        print('2个列表参数不一致')
        return None
    return temp
def main():
    try:
        data_file=input('请输入数据文件名：')
        compare_file=input('请输入匹配文件名：')
        result_file=datetime.now().strftime('%Y%m%d_%H%M%S.xls')
        list1=['货号','自编码/条码','商品名称','规格','单位','产地','货商','进价','零售价',
               '最低售价','分类','品牌','装数','会员价1','会员价2','会员价3','批发价1','批发价2',
               '批发价3','促销价','建档人','提成方式','商品性质','建档日期','修改日期','经销方式',
               '联营扣率%','库存上限','库存下限','参与积分','积分比例','毛利率%','本店库存','最小订货量',
               '组合标志','促销开始时间','促销开始时间','提成金额','状态','是否管理序列号','销售仓库','同码系列',
               '拼音简码','折价','管理库存','其它1','其它2','期初库存','货架号'];
        list2=[];
        for i in range(len(list1)):
            list2.append(i)
        print(list2)
        dict_bak=dict_init(list1,list2);
        ori_data=getExcelList(data_file)[1:-1]#获取数据文件内容
        compare_data=getExcelList(compare_file)#获取进货文件内容
        print('原文件个数：'+str(len(ori_data)))
        print('比较文件个数：' + str(len(compare_data)))
        # 提取列表信息   自编码/条码(1)商品名称(2)进价(7)零售价(8)毛利率/利润率%(31)
        #ori_data = extract_list(ori_data, [1,2,7,8,31])
        #处理掉列表中冗余字符串
        for i in range(len(compare_data)):
            compare_data[i][0]=compare_data[i][0].replace(".0","")
        #写入Excel内容
        writeExcel(list1,result_file)
        #列表查找
        result_list=[];
        parttern1=re.compile(r'^[0-9]*?$');
        num_bak = 0;#写入条码总个数初始化
        num_stock = 0;#进货单总个数初始化
        num_manifest = 0 #对应批发商货单顺序号
        supplier_name = ""#批发商初始化
        for i in range(len(compare_data)):
            num = 0;
            result_list_temp = ['',]*len(list1)
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
                    if ori_data[j][1][-len(compare_data[i][0]):]==compare_data[i][0]:
                        temp=ori_data[j];
                        num=num+1;
            if num==1:
                print('条形码匹配成功')
                result_list_temp=temp

            else:
                print('条形码匹配失败')
                result_list_temp=[compare_data[i][0],'匹配失败']
                if num>1:
                    result_list_temp = [compare_data[i][0], '匹配失败：存在多个条码']
            writeExcel(result_list_temp, result_file)
            num_bak=num_bak+1
        writeExcel(['匹配文件总个数为',str(num_stock)], result_file)
        writeExcel(['写入条码个数为',str(num_bak)], result_file)
    except FileNotFoundError:
        print('文件不存在')
        exp=traceback.format_exc()#获取异常信息
        #print(exp)

if __name__=='__main__':
    main()
    print('文件对比完成')





