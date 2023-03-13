#library
#njpythonlibrary
#-------------------
import paramiko
import time
#-------------------
def connect(server_ip, server_user, server_pwsd):
  sshclient123 = paramiko.SSHClient()
  sshclient123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  sshclient123.connect(server_ip, username=server_user, password=server_pwsd, look_for_keys=False, allow_agent=False)
  return sshclient123
#-------------------
def get_shell(sshclient123):
  netconnection123 = sshclient123.invoke_shell()
  return netconnection123
#-------------------
def send_command(netconnection123, commands):
  netconnection123.send(commands + "\n")
  time.sleep(5)
  out123 = netconnection123.recv(5000)
  return out123
#-------------------
def close(sshclient123):
   sshclient123.close()
#-------------------
