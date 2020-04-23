# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
----------------------------------------------------------------------
@author  :30000367
@time    :2020/03/30
@file    :sdc_connect_by_ssh.py
@desc    :连接carrier客户端
@license :(c) Copyright 2020, SDC.
-----------------------------------------------------------------------
"""
import socket
import paramiko


class SDCConnectException(Exception):
    pass


class SDCConnectBySSH:
    def __init__(self, host, username, pwd, port=22):
        self.host = host
        self.port = port
        self.username = username
        self.pwd = pwd
        self.__transport = None

    def connect(self):
        try:
            transport = paramiko.Transport((self.host, self.port))
            transport.connect(username=self.username, password=self.pwd)
            self.__transport = transport
        except paramiko.AuthenticationException:
            raise SDCConnectException("Authentication failed when connecting to " + self.host)
        except paramiko.ssh_exception.NoValidConnectionsError:
            raise SDCConnectException("please check ssh switch, Unable to connect to port 22 on " + self.host)
        except socket.error:
            raise SDCConnectException("SSHException please Check the net link to server " + self.host)

    def close(self):
        self.__transport.close()

    def upload(self, local_path, target_path):
        # 连接，上传
        # file_name = self.create_file()
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        # 将location.py 上传至服务器 /tmp/test.py
        sftp.put(local_path, target_path)

    def download(self, remote_path, local_path):
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        sftp.get(remote_path, local_path)

    def send_command(self, command):
        try:
            print('user exec command:{}'.format(command))
            _instance = paramiko.SSHClient()
            _instance._transport = self.__transport
            # 执行命令
            stdin, stdout, stderr = _instance.exec_command(command)
            # 执行失败
            exit_status = stdout.channel.recv_exit_status()
            if exit_status != 0:
                stderr_result = stderr.readlines()
                return False, stderr_result
            # 获取命令结果
            stdout_result = stdout.readlines()
            return True, stdout_result
        except paramiko.SSHException:
            raise SDCConnectException('raise exec command')


if __name__ == "__main__":
    ssh = SDCConnectBySSH(host='3.140.35.184', port=22, username='admin', pwd='ChangeMe123')
    ssh.connect()
    print(ssh.send_command("ls /; ifconfig"))
    # ssh.send_command("pwd")
    ssh.close()
