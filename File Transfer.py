from netmiko import ConnectHandler, file_transfer

devicesinfo = {
    "ip": "192.168.100.230",
    'username': "admin",
    "password": "cisco",
    "device_type": "cisco_ios",
}

ssh123 = ConnectHandler(**devicesinfo)
print("ssh connection established ", ssh123)
filetransfer123=file_transfer(ssh123,source_file=r"C:\Users\younus\Desktop\python scripts\Logfiles\test.txt",dest_file=r"new1.txt",file_system="disk0:",direction="put")