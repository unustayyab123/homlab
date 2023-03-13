from netmiko import ConnectHandler, file_transfer
from netmiko.ssh_autodetect import SSHDetect
import logging
logging.basicConfig(filename='ospflogging2.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")
multidevice = ['192.168.100.230','192.168.100.210']
for device in multidevice:
    device = {
        "device_type": "autodetect",
        'ip': device,
        'username': 'admin',
        'password': 'cisco',
        "conn_timeout": 60,
        "session_timeout": 60,
         }
    guesser = SSHDetect(**device)
    best_match = guesser.autodetect()
    print(best_match)
    if best_match == "cisco_ios":
        ssh123 = ConnectHandler(**device)
        print("ssh connection established ", ssh123)
        filetransfer123 = file_transfer(ssh123, source_file=r"C:\Users\younus\Desktop\python scripts\Logfiles\test.txt",
                                        dest_file=r"new.txt", file_system="disk0:", direction="put")
        # print("File transfer is successfull")
        # print(ssh123.send_command("show ip int br"))
    else:
        # ssh123 = ConnectHandler(**device)
        # print("ssh connection established ", ssh123)
        # print(ssh123.send_command("show ip int br"))
        # filetransfer123 = file_transfer(ssh123, source_file=r"C:\Users\younus\Desktop\python scripts\Logfiles\test1.txt",
        #                                 dest_file=r"new.txt", file_system="/mnt/flash", direction="put")
        print("File transfer is successfull")

from netmiko import ConnectHandler
from netmiko.ssh_autodetect import SSHDetect

multidevice = ['192.168.100.230']
for singledevice in multidevice:
    device = {
        "device_type": "autodetect",
        'ip': singledevice,
        'username': 'admin',
        'password': 'cisco'}
    guesser = SSHDetect(**device)
    best_match = guesser.autodetect()
    print(best_match)
    if best_match == 'cisco_ios':
        device1 = {
            "device_type": best_match,
            'ip': singledevice,
            'username': 'admin',
            'password': 'cisco'}

        ssh123 = ConnectHandler(**device1)
        print(ssh123.send_command("show ip int br"))
    # elif best_match == 'cisco_wlc':
    #
    # elif best_match == 'junos':









