#PARAMIKO EXEC_COMMAND
import paramiko
sshclient123 = paramiko.SSHClient()
sshclient123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshclient123.connect("192.168.100.220", username="admin", password="cisco", look_for_keys=False,
                     allow_agent=False)
stdin, stdout, stderr = sshclient123.exec_command("show run")
output123 = stdout.read().decode()
print(output123)
