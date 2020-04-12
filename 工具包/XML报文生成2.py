# -*- coding: utf-8 -*-


import xml.dom.minidom as Dom
from xml.dom import minidom
import random
import time


# 这个方法用来代替minidom里格式化代码，实现节点不换行
def fixed_writexml(self, writer, indent="", addindent="", newl=""):
    # indent = current indentation
    # addindent = indentation to add to higher levels
    # newl = newline string
    writer.write(indent + "<" + self.tagName)
    attrs = self._get_attributes()
    a_names = attrs.keys()
    a_names.sort()

    for a_name in a_names:
        writer.write(" %s=\"" % a_name)
        minidom._write_data(writer, attrs[a_name].value)
        writer.write("\"")
    if self.childNodes:
        if len(self.childNodes) == 1 \
                and self.childNodes[0].nodeType == minidom.Node.TEXT_NODE:
            writer.write(">")
            self.childNodes[0].writexml(writer, "", "", "")
            writer.write("</%s>%s" % (self.tagName, newl))
            return
        writer.write(">%s" % (newl))
        for node in self.childNodes:
            if node.nodeType is not minidom.Node.TEXT_NODE:
                node.writexml(writer, indent + addindent, addindent, newl)
        writer.write("%s</%s>%s" % (indent, self.tagName, newl))
    else:
        writer.write("/>%s" % (newl))


minidom.Element.writexml = fixed_writexml


def write():
    doc = Dom.Document()
    root_node = doc.createElement("service")
    doc.appendChild(root_node)

    head = doc.createElement("SYS_HEAD")
    body = doc.createElement("BODY")

    # SERVICE_CODE
    service_node = doc.createElement("SERVICE_CODE")
    service_value = doc.createTextNode("11005000004")
    service_node.setAttribute("attr", "field")
    service_node.appendChild(service_value)
    head.appendChild(service_node)

    # SERVICE_SCENE
    scene_node = doc.createElement("SERVICE_SCENE")
    scene_value = doc.createTextNode("03")
    scene_node.setAttribute("attr", "field")
    scene_node.appendChild(scene_value)
    head.appendChild(scene_node)

    # CONSUMER_ID
    consumer_node = doc.createElement("CONSUMER_ID")
    consumer_value = doc.createTextNode("033500")
    consumer_node.setAttribute("attr", "field")
    consumer_node.appendChild(consumer_value)
    head.appendChild(consumer_node)

    # CONSUMER_SEQ_NO
    seq_node = doc.createElement("CONSUMER_SEQ_NO")
    seq = 133100201803220002704750 + random.randint(1, 10000)
    seq_value = doc.createTextNode('%d' % seq)
    seq_node.setAttribute("attr", "field")
    seq_node.appendChild(seq_value)
    head.appendChild(seq_node)

    # BUSS_SEQ_NO
    bus_node = doc.createElement("BUSS_SEQ_NO")
    bus_value = doc.createTextNode("2018032284584195")
    bus_node.setAttribute("attr", "field")
    bus_node.appendChild(bus_value)
    head.appendChild(bus_node)

    # TRAN_FLAG
    flag_node = doc.createElement("TRAN_FLAG")
    flag_value = doc.createTextNode("0")
    flag_node.setAttribute("attr", "field")
    flag_node.appendChild(flag_value)
    head.appendChild(flag_node)

    # TRAN_DATE
    date_node = doc.createElement("TRAN_DATE")
    date_value = doc.createTextNode(time.strftime('%Y%m%d'))
    date_node.setAttribute("attr", "field")
    date_node.appendChild(date_value)
    head.appendChild(date_node)

    # TRAN_TIMESTAMP
    time_node = doc.createElement("TRAN_TIMESTAMP")
    time_value = doc.createTextNode("000014")
    time_node.setAttribute("attr", "field")
    time_node.appendChild(time_value)
    head.appendChild(time_node)

    c_node = doc.createElement("END_DATE")
    c_value = doc.createTextNode("20180322")
    c_node.setAttribute("attr", "field")
    c_node.appendChild(c_value)
    body.appendChild(c_node)

    root_node.appendChild(head)
    root_node.appendChild(body)
    print(doc.toxml("utf-8"))
    f = open("ttt.xml", "w")
    f.write(doc.toprettyxml(indent="\t", newl="\n", encoding="utf-8"))
    f.close()


if __name__ == "__main__":
    write()
