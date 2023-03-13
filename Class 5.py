from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException

from datetime import datetime
import logging
logging.basicConfig(filename='ospflogging.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

#Enter Device Details
multidevice = open(r"C:\Users\younus\Desktop\python scripts\devicename.txt", )
listofdevices = multidevice.read().splitlines()

user123 = open(r"C:\Users\younus\Desktop\python scripts\devicecred.txt", )
readuser = user123.read().splitlines()[0]

pass123 = open(r"C:\Users\younus\Desktop\python scripts\devicecred.txt", )
readpass = pass123.read().splitlines()[1]

for device in listofdevices:
    devicesinfo = {
    "ip": device,
    'username': readuser,
    "password": readpass,
    "device_type": "cisco_ios",
    }

    try:
        ssh123 = ConnectHandler(**devicesinfo)  # ssh is stablshd
        print("Connected to " + device)
        hostname123 = ssh123.find_prompt()
        newhostname123 = hostname123[0:-1]
        print(newhostname123)

        cmds123 = ["router ospf 100", "network 192.168.100.0 0.0.0.255 area 0"]
        config123 = ssh123.send_config_set(cmds123)
        print(config123)
        neighruptime = ssh123.send_command("sh ip ospf neighbor fastEthernet 0/0 detail | i up")
        print(neighruptime)

        clearospf = ssh123.send_command_timing("clear ip ospf process")
        print(clearospf)
        if "Reset in clearospf":
            print("OSPF AVAILABLE")
            #input123 = input("Enter yes|No to clear the ospf process :")
            #if "yes" in input123:
                #ssh123.write_channel(input123)
                #ssh123.write_channel("\n")
                #neighruptime123 = ssh123.send_command("sh ip ospf neighbor fastEthernet 0/0 detail | i up")
                #print(neighruptime123)
            #else:
                #print("Reset process declined by user")
        else:
            print("OSPF NOT CONFIGURED")

        print(" Disconnected from " + device)
    except NetMikoAuthenticationException:
        print("Device failed due to Authentication " + device)
        createemptyfile123 = open(r"C:\Users\younus\Desktop\python scripts\Logfiles\Authentication_Issues.txt", "a")
        copycontent123 = createemptyfile123.write(device)

    except NetMikoTimeoutException:
        print("Device IP Not Reachable \n" + device)
        createemptyfile1234 = open(r"C:\Users\younus\Desktop\python scripts\Logfiles\Device-unreachanble-Issues.txt", "a")
        copycontent1234 = createemptyfile1234.write(device)

