# -*- coding: gbk -*-
#连接SFTP 创建多级目录


import paramiko


def sftpMkdir(host,port,username,password,filePath):
    
    '''
    host        str    ip地址
    port        int    端口
    username    str    用户
    password    str    密码
    filePath    str    本地路径
    '''
    
    #获取Transport实例
    sf = paramiko.Transport((host,port));
    #连接SSH服务端,使用password
    sf.connect(username = username,password = password)
    #创建一个已连通的SFTP客户端通道
    sftp = paramiko.SFTPClient.from_transport(sf)
    catalog=filePath.split("/");
    if len(catalog)>2:
        pathApeend="";
        for i in catalog[1:-1]:
            try:
                 pathApeend=pathApeend+"/"+i;
                 sftp.mkdir(pathApeend,mode=755);
                 print("目录创建成功："+pathApeend)
            except IOError:
                print(pathApeend+"[该目录已存在或无权限创建目录]");
            continue;
    else:
        print("上传路径为根路径，无需创建目录");

    sf.close();
        

#host='10.91.131.234';
#port=2222;

host='10.91.130.202';
port=22;
username="xfzf";
password="xfzf";
filePath="/BBB/AA.txt";

sftpMkdir(host,port,username,password,filePath)



    
    
    
    
