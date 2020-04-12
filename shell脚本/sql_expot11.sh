#!/bin/bash  导出数据
aaa=`echo $TZ|sed 's/.*\(..\)/\1/'`
 aaa=`expr $aaa + 24`
 eval aaa=`echo $TZ|sed 's/..$/+$aaa/'`
 TZ=$aaa
 export TZ
 yy=`date +%y`
 mm=`date +%m`
 dd=`date +%d`
 echo $mm$dd$yy





