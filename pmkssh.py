# -*- coding: utf-8 -*-

from paramiko import SSHClient
import paramiko

class SSH:
    def __init__(self):
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def conn(self,host,user,passw):
        try:
            self.ssh.connect(hostname=host,username=user,password=passw)
        except Exception:
            self.connected = False
        else:
            self.connected = True 

    def exec_cmd(self,cmd):
        if self.connected:
            stdin,stdout,stderr = self.ssh.exec_command(cmd)
            if stderr.channel.recv_exit_status() != 0:
                return stderr
            else:
                return stdout

if __name__ == '__main__':
    # Exemplo de uso da classe SSH
    # Antes da chamada é necessário definir as variáveis: host user passw
    host = 'IP Address'
    user = 'Nome do usuário que fará a conexão'
    passw = 'Password do usuário'
    ssh = SSH()
    ssh.conn(host,user,passw)
    output = ssh.exec_cmd("ls -l;hostname;date")
    for i in output:
        print(i.rstrip('\n'))
