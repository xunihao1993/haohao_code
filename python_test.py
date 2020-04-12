#coding=utf-8 

##############################  1.解析xml  ################################################################
#'''
#coding=utf-8 
  
from xml.dom.minidom import parse 
import xml.dom.minidom 
  
# 使用minidom解析器打开XML文档 
DOMTree = xml.dom.minidom.parse("I:\\country.xml") 
Data = DOMTree.documentElement 
if Data.hasAttribute("name"): 
  print "name element : %s" % Data.getAttribute("name") 
 
# 在集合中获取所有国家 
Countrys = Data.getElementsByTagName("country") 
  
# 打印每个国家的详细信息 s
for Country in Countrys: 
  print "*****Country*****"
  if Country.hasAttribute("name"): 
   print "name: %s" % Country.getAttribute("name") 
  
  rank = Country.getElementsByTagName('rank')[0] 
  print "rank: %s" % rank.childNodes[0].data 
  year = Country.getElementsByTagName('year')[0] 
  print "year: %s" % year.childNodes[0].data 
  gdppc = Country.getElementsByTagName('gdppc')[0] 
  print "gdppc: %s" % gdppc.childNodes[0].data 
  
  for neighbor in Country.getElementsByTagName("neighbor"):  
    print neighbor.tagName, ":", neighbor.getAttribute("name"), neighbor.getAttribute("direction")

#'''
########################################################################################################
