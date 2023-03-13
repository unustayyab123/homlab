from netmiko import ConnectHandler, file_transfer
device1={
        "device_type": 'arista_eos',
        'ip': '192.168.100.190',
        'username': 'admin',
        'password': 'cisco',
        "conn_timeout": 60,
        "session_timeout": 60,
        }
ssh123 = ConnectHandler(**device1)
print("ssh connection established ", ssh123)
filetransfer123 = file_transfer(ssh123, source_file=r"C:\Users\younus\Desktop\networkjourney\network.txt",
                    dest_file=r"network1.txt", file_system="/mnt/flash", direction="put")
print("File transfer is successfull")