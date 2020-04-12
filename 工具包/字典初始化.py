
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

list1=['1','2','哈哈','']
list2=['a','b','','']
print(dict_init(list1,list2))