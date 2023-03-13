import njpythonlibrary
import logging

logging.basicConfig(filename='njpythonlibrary_global.log', level=logging.DEBUG)
logger = logging.getLogger("njpythonlibrary")
sshclient = njpythonlibrary.connect("192.168.100.220", "admin", "cisco")
remote123 = njpythonlibrary.get_shell(sshclient)

output123 = njpythonlibrary.send_command(remote123,"show clock")
print(output123.decode())
output123 = njpythonlibrary.send_command(remote123,"show ip int br")
print(output123.decode())
output123 = njpythonlibrary.send_command(remote123,"show run | i hostname")
print(output123.decode())
output123 = njpythonlibrary.send_command(remote123,"show version")
print(output123.decode())
njpythonlibrary.close(sshclient)