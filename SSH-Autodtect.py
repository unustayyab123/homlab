from netmiko import ConnectHandler
from netmiko.ssh_autodetect import SSHDetect
readmultidevice123 = ["192.168.100.220"]
for singledevice in readmultidevice123:
            devicedictionary = {
                "ip": singledevice,
                "username": "admin",
                "password": "admin",
                "device_type": "autodetect", #ro
            }
            gueser123 = SSHDetect(**devicedictionary)
            device_type123 = gueser123.autodetect()
            print(device_type123)
