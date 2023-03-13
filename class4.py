from netmiko import ConnectHandler
from datetime import datetime
mytimenow= datetime.now()
import schedule
import time

#Enter Device Details
multidevice = open(r"C:\Users\younus\Desktop\python scripts\devicename.txt", )
listofdevices = multidevice.read().splitlines()
    # print(listofdevices)

#Enter Device credential
user123 = open(r"C:\Users\younus\Desktop\python scripts\devicecred.txt", )
readuser = user123.read().splitlines()[0]

pass123 = open(r"C:\Users\younus\Desktop\python scripts\devicecred.txt", )
readpass = pass123.read().splitlines()[1]

def mybackup():
    print("Backup in Progress")
    for device in listofdevices:
        devicesinfo = {
                "ip": device,
                'username': readuser,
                "password": readpass,
                "device_type": "cisco_ios",
        }
        ssh123 = ConnectHandler(**devicesinfo)  # ssh is stablshd
        print("Connected to " + device)
        hostname123 = ssh123.find_prompt()
        newhostname123 = hostname123[0:-1]
        # print(newhostname123)

        multiplecli123 = ["show clock", "show ip int brief", "show ip arp", "show ip route", "show run | i hostname"]
        for cli in multiplecli123:
            config123 = ssh123.send_command(cli)
            print("*" * 10 + "output for" + cli)
            print(ssh123.send_command(cli))

        # cmds123=["logging host 1.1.1.1","router ospf1 100" ,"logging host 2.2.2.2"]
        #     config123=ssh123.send_config_set(cmds123)
        # print(config123)
            createlogfile = open(r"C:\Users\younus\Desktop\python scripts\Logfiles\logs_" + device + "-" + newhostname123 + "#" +
            str(mytimenow.year) + "-" + str(mytimenow.month) + "-" + str(mytimenow.day) + "-" + str(mytimenow.microsecond) + "-" + ".txt", "a")
            copycontent123=createlogfile.write(config123)
            createlogfile.close()
            print(" Disconnected from " + device)
schedule.every(10).seconds.do(mybackup)
while True:
    schedule.run_pending()
    time.sleep(1)