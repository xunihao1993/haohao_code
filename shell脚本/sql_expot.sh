#!/bin/bash  导出数据
DB2_HOME=/opt/IBM/db2/V10.5   #引入db2的环境路径
PATH=$DB2_HOME/bin:$PATH
export $DB2_HOME
export $PATH
DATANAME="DB4CNAPS"             #数据库名称
DATAUSER="cnapsi"               #用户名
DATARPASSWD="cnapsi"            #密码
cus_date=$(date +"%Y%m%d" -d "-1 days");
echo "connect to db2"
db2 connect to $DATANAME user $DATAUSER using $DATARPASSWD;
db2 "export to 20181001-1007_bak/"$cus_date"大额借记来账.txt of del select count(1),sum(bigint(amount)) from t_hvps_paymentbook t where workdate >= '"$cus_date"' and workdate<='"$cus_date"'  and mbflag='2'and PAYFLAG='2' and centerstatus='PR04'group by workdate" ;
db2 "export to 20181001-1007_bak/"$cus_date"大额借记往账.txt of del select count(1),sum(bigint(amount)) from t_hvps_paymentbook t where workdate >= '"$cus_date"' and  workdate<='"$cus_date"'  and mbflag='1'and PAYFLAG='2' and centerstatus='PR04'group by workdate" ;
db2 "export to 20181001-1007_bak/"$cus_date"大额贷记往帐.txt of del select count(1),sum(bigint(amount)) from t_hvps_paymentbook t where workdate >= '"$cus_date"' and workdate<='"$cus_date"' and mbflag='1' AND PAYFLAG='1'  and centerstatus='PR04'group by workdate" ;
db2 "export to 20181001-1007_bak/"$cus_date"大额贷记来账.txt of del select count(1),sum(bigint(amount)) from t_hvps_paymentbook t where workdate >= '"$cus_date"' and workdate<='"$cus_date"' and mbflag='2' AND PAYFLAG='1'  and centerstatus='PR04'group by workdate" ;
db2 "export to 20181001-1007_bak/"$cus_date"小额借记来账.txt of del select count(1),sum(bigint(amount)) from t_beps_paymentbook t where workdate >= '"$cus_date"' and workdate<='"$cus_date"'  and mbflag='2'and PAYFLAG='2' and centerstatus='PR04'group by workdate" ;
db2 "export to 20181001-1007_bak/"$cus_date"小额借记往账.txt of del select count(1),sum(bigint(amount)) from t_beps_paymentbook t where workdate >= '"$cus_date"' and workdate<='"$cus_date"'  and mbflag='1'and PAYFLAG='2' and centerstatus='PR04'group by workdate" ;
db2 "export to 20181001-1007_bak/"$cus_date"小额贷记往帐.txt of del select count(1),sum(bigint(amount)) from t_beps_paymentbook t where workdate >= '"$cus_date"' and workdate<='"$cus_date"' and mbflag='1' AND PAYFLAG='1'  and centerstatus='PR04'group by workdate" ;
db2 "export to 20181001-1007_bak/"$cus_date"小额贷记来账.txt of del select count(1),sum(bigint(amount)) from t_beps_paymentbook t where workdate >= '"$cus_date"' and workdate<='"$cus_date"' and mbflag='2' AND PAYFLAG='1'  and centerstatus='PR04'group by workdate" ;
db2 "export to 20181001-1007_bak/"$cus_date"超网借记来账.txt of del select count(1),sum(bigint(amount)) from t_ibps_paymentbook t where workdate >= '"$cus_date"' and workdate<='"$cus_date"'  and mbflag='2'and PAYFLAG='2' and centerstatus='PR04' group by workdate" ;
db2 "export to 20181001-1007_bak/"$cus_date"超网借记来账.txt of del select count(1),sum(bigint(amount)) from t_ibps_paymentbook t where workdate >= '"$cus_date"' and workdate<='"$cus_date"'  and mbflag='1'and PAYFLAG='2' and centerstatus='PR04' group by workdate" ;
db2 "export to 20181001-1007_bak/"$cus_date"超网借记来账.txt of del select count(1),sum(bigint(amount)) from t_ibps_paymentbook t where workdate >= '"$cus_date"' and workdate<='"$cus_date"' and mbflag='1' AND PAYFLAG='1'  and centerstatus='PR04' group by workdate" ;
db2 "export to 20181001-1007_bak/"$cus_date"超网借记来账.txt of del select count(1),sum(bigint(amount)) from t_ibps_paymentbook t where workdate >= '"$cus_date"' and workdate>='"$cus_date"' and mbflag='2' AND PAYFLAG='1'  and centerstatus='PR04' group by workdate" ;









