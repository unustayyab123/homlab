import netmiko
import time
start = time.time()
from netmiko import ConnectHandler
multipledevice123 = ["192.168.100.220", "192.168.100.221","192.168.100.230"]
for singledevice in multipledevice123:
    information123 = {
        "device_type": "cisco_ios",
        "ip": singledevice,
        "username": "admin",
        'password': "cisco",
    }
    ssh123 = ConnectHandler(**information123)
    output=ssh123.send_config_from_file(r"C:\Users\younus\Desktop\python scripts\commands.txt")
    print(output)

end = time.time()
elapstime = end-start
print(elapstime)