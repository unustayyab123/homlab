from netmiko import ConnectHandler, file_transfer
from netmiko.ssh_autodetect import SSHDetect


multidevice = ["192.168.100.190", "192.168.100.230"]
best_match = ["arista_eos", "cisco_ios"]
for singledevice in multidevice:
    device = {
        "device_type": best_match,
        'ip': singledevice,
        'username': 'admin',
        'password': 'cisco',
        # "conn_timeout": 60,
        # "session_timeout": 60,
         }
    if best_match()[0] == "arista_eos":
        device1={
        "device_type": best_match,
        'ip': singledevice,
        'username': 'admin',
        'password': 'cisco',
        "conn_timeout": 60,
        "session_timeout": 60,
        }
        # ARISTA DEVICE FILE TRANSFER
        ssh123 = ConnectHandler(**device1)
        print("ssh connection established ", ssh123)
        # filetransfer123 = file_transfer(ssh123, source_file=r"C:\Users\younus\Desktop\networkjourney\network.txt",
        #                                 dest_file=r"network1.txt", file_system="/mnt/flash", direction="put")
        # print("File transfer is successfull")
    else:

        #CISCO DEVICE FILE TRANSFER
        ssh123 = ConnectHandler(**device1)
        print("ssh connection established ", ssh123)
        # filetransfer123 = file_transfer(ssh123, source_file=r"C:\Users\younus\Desktop\networkjourney\network.txt",
        # dest_file=r"test5.txt", file_system="disk0:", direction="put")
        # print("File transfer is successfull")


