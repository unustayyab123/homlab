from netmiko import ConnectHandler
from getpass import getpass

from datetime import datetime
mytimenow= datetime.now()
#Enter device Password
passwordEnter = getpass("enter the password for : ")

multidevice = ["192.168.100.220","192.168.100.230"]
for device in multidevice:
    devicesinfo={
        "ip": device,
        'username': "admin",
        "password": passwordEnter,
        "device_type": "cisco_ios",
    }

    ssh123 = ConnectHandler(**devicesinfo)     #ssh is stablshd
    print("Connected to " + device)
    hostname123 = ssh123.find_prompt()
    newhostname123 = hostname123[0:-1]
    print(newhostname123)

    multiplecli123 = ["show ip int brief", "show ip route"]
    for cli in multiplecli123:
        print("*" * 10 + "output for" + cli)
        print(ssh123.send_command(cli))

    cmds123=["logging host 1.1.1.1","router ospf1 100" ,"logging host 2.2.2.2"]
    config123=ssh123.send_config_set(cmds123)
    print(config123)
    createlogifile=open(r"C:\Users\younus\Desktop\python scripts\Logfiles\logs_" + device + "-" +  newhostname123 +"#" +
                    str(mytimenow.year) + "-" + str(mytimenow.month) + "-"+ str(mytimenow.day) + ".txt","a")
    copycontent123=createlogifile.write(config123)
    createlogifile.close
    print(" Disconnected from " + device)