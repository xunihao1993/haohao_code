#!/bin/bash  ��������
DB2_HOME=/opt/IBM/db2/V10.5   #����db2�Ļ���·��
PATH=$DB2_HOME/bin:$PATH
export $DB2_HOME
export $PATH
DATANAME="DB4CNAPS"             #���ݿ�����
DATAUSER="cnapsi"               #�û���
DATARPASSWD="cnapsi"            #����
cus_date=$(date +"%Y%m%d" -d "-1 days");
echo "connect to db2"
db2 connect to $DATANAME user $DATAUSER using $DATARPASSWD;
db2 "export to 20181001-1007_bak/"$cus_date"���������.txt of del select count(1),sum(bigint(amount)) from t_hvps_paymentbook t where workdate >= '"$cus_date"' and workdate<='"$cus_date"'  and mbflag='2'and PAYFLAG='2' and centerstatus='PR04'group by workdate" ;
db2 "export to 20181001-1007_bak/"$cus_date"���������.txt of del select count(1),sum(bigint(amount)) from t_hvps_paymentbook t where workdate >= '"$cus_date"' and  workdate<='"$cus_date"'  and mbflag='1'and PAYFLAG='2' and centerstatus='PR04'group by workdate" ;
db2 "export to 20181001-1007_bak/"$cus_date"����������.txt of del select count(1),sum(bigint(amount)) from t_hvps_paymentbook t where workdate >= '"$cus_date"' and workdate<='"$cus_date"' and mbflag='1' AND PAYFLAG='1'  and centerstatus='PR04'group by workdate" ;
db2 "export to 20181001-1007_bak/"$cus_date"����������.txt of del select count(1),sum(bigint(amount)) from t_hvps_paymentbook t where workdate >= '"$cus_date"' and workdate<='"$cus_date"' and mbflag='2' AND PAYFLAG='1'  and centerstatus='PR04'group by workdate" ;
db2 "export to 20181001-1007_bak/"$cus_date"С��������.txt of del select count(1),sum(bigint(amount)) from t_beps_paymentbook t where workdate >= '"$cus_date"' and workdate<='"$cus_date"'  and mbflag='2'and PAYFLAG='2' and centerstatus='PR04'group by workdate" ;
db2 "export to 20181001-1007_bak/"$cus_date"С��������.txt of del select count(1),sum(bigint(amount)) from t_beps_paymentbook t where workdate >= '"$cus_date"' and workdate<='"$cus_date"'  and mbflag='1'and PAYFLAG='2' and centerstatus='PR04'group by workdate" ;
db2 "export to 20181001-1007_bak/"$cus_date"С���������.txt of del select count(1),sum(bigint(amount)) from t_beps_paymentbook t where workdate >= '"$cus_date"' and workdate<='"$cus_date"' and mbflag='1' AND PAYFLAG='1'  and centerstatus='PR04'group by workdate" ;
db2 "export to 20181001-1007_bak/"$cus_date"С���������.txt of del select count(1),sum(bigint(amount)) from t_beps_paymentbook t where workdate >= '"$cus_date"' and workdate<='"$cus_date"' and mbflag='2' AND PAYFLAG='1'  and centerstatus='PR04'group by workdate" ;
db2 "export to 20181001-1007_bak/"$cus_date"�����������.txt of del select count(1),sum(bigint(amount)) from t_ibps_paymentbook t where workdate >= '"$cus_date"' and workdate<='"$cus_date"'  and mbflag='2'and PAYFLAG='2' and centerstatus='PR04' group by workdate" ;
db2 "export to 20181001-1007_bak/"$cus_date"�����������.txt of del select count(1),sum(bigint(amount)) from t_ibps_paymentbook t where workdate >= '"$cus_date"' and workdate<='"$cus_date"'  and mbflag='1'and PAYFLAG='2' and centerstatus='PR04' group by workdate" ;
db2 "export to 20181001-1007_bak/"$cus_date"�����������.txt of del select count(1),sum(bigint(amount)) from t_ibps_paymentbook t where workdate >= '"$cus_date"' and workdate<='"$cus_date"' and mbflag='1' AND PAYFLAG='1'  and centerstatus='PR04' group by workdate" ;
db2 "export to 20181001-1007_bak/"$cus_date"�����������.txt of del select count(1),sum(bigint(amount)) from t_ibps_paymentbook t where workdate >= '"$cus_date"' and workdate>='"$cus_date"' and mbflag='2' AND PAYFLAG='1'  and centerstatus='PR04' group by workdate" ;









