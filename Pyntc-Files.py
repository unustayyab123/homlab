#PYNTC MODULE
import json
# from pyntc import ntc_device as NTC123
# ios123=NTC123(host="192.168.100.230" ,username="admin",password="cisco",device_type="cisco_ios_ssh")
# ios123.open()
# CMD123=["show ip int brief", "show clock"]
# for command in CMD123:
#     output123=ios123.show(command)
#     print(output123, '\n')

# # for command in CMD123:
# output123=ios123.config(["logging host 1.1.1.1","logging host 2.1.2.1"])
# out123=json.dumps(output123,sort_keys="True",indent=4)
# print(out123, '\n')

# # backing up
# output123=ios123.running_config
# print(output123)

#backing up
# output123=ios123.running_config
# createnotepad=open(r"C:\Users\younus\Desktop\networkjourney\backup\backup-192.168.100.230.txt" ,"w")
# writecontent=createnotepad.write(output123)
# output123=ios123.running_config
# createnotepad.close()

#Backup-Easy Method
# from pyntc import ntc_device as NTC123
# ios123=NTC123(host="192.168.100.230" ,username="admin",password="cisco",device_type="cisco_ios_ssh")
# ios123.open()
# output123 = ios123.backup_running_config("backup-new-192.168.100.230")
# ios123.close()

#file copy
# from pyntc import ntc_device as NTC123
# ios123 = NTC123(host="192.168.100.230" ,username="admin",password="cisco",device_type="cisco_ios_ssh")
# ios123.open()
# output123 = ios123.file_copy("backup-new-192.168.100.230")
# ios123.close()

# from pyntc import ntc_device as NTC123
# ios123 = NTC123(host="192.168.100.230" ,username="admin",password="cisco",device_type="cisco_ios_ssh")
# ios123.open()
# ios123.close()

#IOS UPGRADE
from pyntc import ntc_device as NTC123
multidevice = ["192.168.100.239"]
for singledevice in multidevice:
    ios123 = NTC123(host=singledevice, username="admin", password="cisco", device_type='f5_tmos_icontrol')
    ios123.open()
    output123 = ios123.file_copy("any.bin")
    ios123.install_os("any.bin")
    ios123.reboot(confirm=True, timer=5)



