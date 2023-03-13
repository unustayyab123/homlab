#PARAMIKO INVOKE_COMMAND
import paramiko
import time
sshclient123 = paramiko.SSHClient()
sshclient123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshclient123.connect("192.168.100.220", username="admin", password="cisco", look_for_keys=False,
                     allow_agent=False)
netconnect123 = sshclient123.invoke_shell()
netconnect123.send(b"show ip int brief\n")
netconnect123.send(b"show clock\n")
netconnect123.send(b"show run | i hostname\n")
netconnect123.send(b"show version\n")
time.sleep(15)
output123 = netconnect123.recv(50000)
print(output123.decode())
