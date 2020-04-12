# -*- coding: utf-8 -*-
# -*- coding:utf8 -*- # 避免中文乱码

import xml.dom.minidom as Dom
import random
import time

def main():

    #======================构建文档，创建根节点===================#
    doc = Dom.Document() # 创建Dom文档对象
    ROOT = doc.createElement("root") # 创建根节点
    doc.appendChild(ROOT) # 构建根节点

    # ======================开始生成对象树=======================#
    # ======================创建子节点===========================#
    # COUNT
    COUNT = doc.createElement("count") # 创建子节点
    ROOT.appendChild(COUNT) # 向根节点下构建子节点

    # COUNT_CONTEXT
    COUNT_CONTEXT = doc.createTextNode("512") # 创建文本节点内容
    COUNT.appendChild(COUNT_CONTEXT)  # 向子节点添加内容

    # SJMX
    SJMX = doc.createElement("sjmx")
    ROOT.appendChild(SJMX)

    # ======================具体明细1===========================#
    # TBL_NAME
    TBL_NAME = doc.createElement("tableName")
    SJMX.appendChild(TBL_NAME)

    # COLUMN
    COLUMN = doc.createElement("column")
    TBL_NAME.appendChild(COLUMN)

    # COLUMN_CONTEXT
    COLUMN_CONTEXT = doc.createTextNode("column_context")
    COLUMN.appendChild(COLUMN_CONTEXT)

    # ======================具体明细2===========================#
    # TBL_NAME
    TBL_NAME = doc.createElement("tableName")
    SJMX.appendChild(TBL_NAME)

    # COLUMN
    COLUMN = doc.createElement("column1")
    TBL_NAME.appendChild(COLUMN)

    # COLUMN_CONTEXT
    COLUMN_CONTEXT = doc.createTextNode("column_context1")
    COLUMN.appendChild(COLUMN_CONTEXT)

    # ======================生成结束===========================#

    # ======================写入文件===========================#
    f = open("111.xml", "w")   #打开文件,若文件不存在，则自动创建文件，若存在则直接打开
    #调用dom的writexml()方法来将内容写入文件
    #writexml()方法语法格式为 writexml(writer, indent, addindent, newl, encoding)
    #       参数含义：writer是文件对象
    #                indent是每个tag前填充的字符，如：''，则表示每个tag前有两个空格
    #                addindent是每个子结点的缩近字符
    #                newl是每个tag后填充的字符，如：’\n’，则表示每个tag后面有一个回车
    #                encoding是生成的XML信息头中的encoding属性值，在输出时minidom并不真正进行编码的处理，如果你保存的文本内容中有汉字，则需要自已进行编码转换
    #                writexml方法是除了writer参数必须要有外，其余可以省略
    doc.writexml(f, newl = '\n', addindent = '\t',encoding='utf-8')
    print(doc)
    # print(list(doc))
    f.close()


if __name__ == "__main__":
    main()
