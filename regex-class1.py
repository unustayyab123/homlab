from netmiko import ConnectHandler
from getpass import getpass
import re

devicesinfo={
        "ip": "192.168.100.220",
        'username': "admin",
        "password": "cisco",
        "device_type": "cisco_ios",
    }

ssh123 = ConnectHandler(**devicesinfo)
output123 = ssh123.send_command("sh version")
regexout = re.compile(r"\s*uptime\s*is\s*(.+)*")
fetch123=regexout.findall(output123)
print(fetch123)

regexout1 = re.compile(r"(\S+)\s*uptime\s*is")
fetch1231=regexout1.findall(output123)
print(fetch1231)


reload = re.compile(r"(\S+)\s*reload\s*cause")
reloadreason=reload.findall(output123)
print(reloadreason)

output1231 = ssh123.send_command("show interface FastEthernet0/0")
interface = re.compile(r"\s*Internet\saddress\sis\s(\S+)/")
interfaces=interface.findall(output1231)
print(interfaces)


# print(output123)