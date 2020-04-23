# -*- coding: utf-8 -*-
import json

# 思路：用递归深度遍历查找text
#  用一个键值对字典存储父节点，{子节点1：父节点1，子节点2：父节点2},当找到text的时候从字典依次找到父节点就行


def find(text1):
    global aa  # 每次递归前存储父节点的临时值
    global list22  # 列表类型，用来转换出层级结果（XX.CC.AA）
    global list33  # 字典类型，用来存储父节点
    with open("result.json", 'r', encoding='utf-8') as f:
        jsontest = json.load(f)
    list22 = []
    list33 = {}
    aa = None

    def getNode(json_test, text):
        global aa      # 每次递归前存储父节点
        global list22  # 列表类型，用来转换
        global list33  # 字典类型，用来存储父节点
        for i in range(0,len(json_test)):
            # 判断当前循环体的数据类型：如果是字典则取出所有key值与目标值对比
            if isinstance(json_test,(dict,)):
                json_testKey=list(json_test.keys()) # 如果是字典取出key键对应列表
                mid=json_testKey[i]
                # 为所有节点指向同一个父节点，用字典保存
                for j in json_testKey:
                    # list33[j]=aa
                    list33[j]=list33.get(j,aa)
            # 如果当前循环体是列表或元组，则取出对应i索引的列表值与目标值判断
            if isinstance(json_test,(tuple,list)):
                mid=json_test[i] #
                for j in json_test:
                    if type(j).__name__ == 'str':
                        list33[j] = list33.get(j, aa)
                    if type(j).__name__ == 'dict':
                        for ii in list(j.keys()):
                            list33[ii] = list33.get(ii, aa)

            if text == mid:
                list22.append(text)
                # print('找到元素',text)
                while list33[text] is not None:
                    list22.append(list33[text])
                    text=list33[text]
                list22='.'.join(list22[::-1])

            elif isinstance(json_test, (dict,)):
                if(len(json_test[mid])>=1) and type(json_test[mid]).__name__ != 'str':
                    aa = json_testKey[i]
                    getNode(json_test[json_testKey[i]],text)
            elif isinstance(json_test, (tuple,list)):
                if type(json_test[i]).__name__!='str':
                    getNode(json_test[i], text)
        return list22
    return getNode(jsontest, text1)


if __name__ == '__main__':
    one = find("公历")
    print(one)
    # print(list33)


