import re

def File_Replace(FileName,Re,content):
    list1=[]
    pattern=re.compile(Re)
    with open(FileName,'r',encoding='utf-8') as fp:
        for line in fp:
            temp=pattern.sub(content,line)
            list1.append(temp)
    with open(FileName,'w',encoding='utf-8') as fp:
        for i in list1:
            fp.write(i)



File_Replace('条码.txt',r'\n','\t1\n')
