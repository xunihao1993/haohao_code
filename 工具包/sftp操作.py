# -*- coding: gbk -*-
#����SFTP �����༶Ŀ¼


import paramiko


def sftpMkdir(host,port,username,password,filePath):
    
    '''
    host        str    ip��ַ
    port        int    �˿�
    username    str    �û�
    password    str    ����
    filePath    str    ����·��
    '''
    
    #��ȡTransportʵ��
    sf = paramiko.Transport((host,port));
    #����SSH�����,ʹ��password
    sf.connect(username = username,password = password)
    #����һ������ͨ��SFTP�ͻ���ͨ��
    sftp = paramiko.SFTPClient.from_transport(sf)
    catalog=filePath.split("/");
    if len(catalog)>2:
        pathApeend="";
        for i in catalog[1:-1]:
            try:
                 pathApeend=pathApeend+"/"+i;
                 sftp.mkdir(pathApeend,mode=755);
                 print("Ŀ¼�����ɹ���"+pathApeend)
            except IOError:
                print(pathApeend+"[��Ŀ¼�Ѵ��ڻ���Ȩ�޴���Ŀ¼]");
            continue;
    else:
        print("�ϴ�·��Ϊ��·�������贴��Ŀ¼");

    sf.close();
        

#host='10.91.131.234';
#port=2222;

host='10.91.130.202';
port=22;
username="xfzf";
password="xfzf";
filePath="/BBB/AA.txt";

sftpMkdir(host,port,username,password,filePath)



    
    
    
    
