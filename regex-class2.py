from netmiko import ConnectHandler
from getpass import getpass
import re
import csv
import os

multidevice=['192.168.100.220','192.168.100.230']

for singledevice in multidevice:
    devicesinfo={
            "ip": singledevice,
            'username': "admin",
            "password": "cisco",
            "device_type": "cisco_ios",
        }

    ssh123 = ConnectHandler(**devicesinfo)
    # print(" Connecting to Device" ,+singledevice)
    output123 = ssh123.send_command("sh version")
    regexout = re.compile(r"\s*uptime\s*is\s*(.+)")
    Uptime=regexout.findall(output123)
    print(Uptime[0])

    regexout1 = re.compile(r"(\S+)\s*uptime\s*is")
    host123=regexout1.findall(output123)
    print(host123[0])


    reload = re.compile(r"(\S+)\s*reload\s*cause")
    reloadreason=reload.findall(output123)
    print(reloadreason[0])


    iosversion123 = re.compile(r"Version\s*(\S+),")
    iosversion1234 = iosversion123.findall(output123)
    print(iosversion1234[0])
    #
    iospath123 = re.compile(r'System\s*image\s*file\s*is\s*"(\S+)"')
    iospath1234 = iospath123.findall(output123)
    print(iospath1234[0])
    #
    serialid123 = re.compile(r'Processor\s*board\s*ID\s*(\S+)')
    serialid1234 = serialid123.findall(output123)
    print(serialid1234[0])
    #
    configregister123 = re.compile(r'Configuration\s*register\s*is\s*(\S+)')
    configregister1234 = configregister123.findall(output123)
    print(configregister1234[0])

    output1231 = ssh123.send_command("show interface FastEthernet0/0")
    ip123 = re.compile(r"\s*Internet\saddress\sis\s(\S+)/")
    ip1234=ip123.findall(output1231)
    print(ip1234[0])

    mask123 = re.compile(r'\s*Internet\s*address\s*is\s*\S+/(\S+)')
    mask1234 = mask123.findall(output1231)
    print(mask1234[0])



    #File check if file exist or not
    excelfilepath123 = os.path.isfile(r"C:\Users\younus\Desktop\python scripts\Logfiles\regexoutputfile.csv")
    if excelfilepath123:
    #csv preparation
        with open(r"C:\Users\younus\Desktop\python scripts\Logfiles\regexoutputfile.csv","a" ,newline="") as csv123:
            header123=["HOSTNAME", "MGMT_IP", "SUBNET_MASK","SERIAL_ID","CURRENT_IOS_VER","IOS_PATH","UPTIME","CONFIG_REGISTER"]
            wr123=csv.DictWriter(csv123, fieldnames=header123)
            # wr123.writeheader()
            wr123.writerow({
                "HOSTNAME":host123[0],
                "MGMT_IP":ip1234[0],
                "SUBNET_MASK":mask1234[0],
                "SERIAL_ID":serialid1234[0],
                "CURRENT_IOS_VER":iosversion1234[0],
                "IOS_PATH":iospath1234[0],
                "UPTIME":Uptime[0],
                "CONFIG_REGISTER":configregister1234[0]
            })
    if not excelfilepath123:
        with open(r"C:\Users\younus\Desktop\python scripts\Logfiles\regexoutputfile.csv","a" ,newline="") as csv123:
            header123=["HOSTNAME", "MGMT_IP", "SUBNET_MASK","SERIAL_ID","CURRENT_IOS_VER","IOS_PATH","UPTIME","CONFIG_REGISTER"]
            wr123=csv.DictWriter(csv123, fieldnames=header123)
            wr123.writeheader()
            wr123.writerow({
                "HOSTNAME":host123[0],
                "MGMT_IP":ip1234[0],
                "SUBNET_MASK":mask1234[0],
                "SERIAL_ID":serialid1234[0],
                "CURRENT_IOS_VER":iosversion1234[0],
                "IOS_PATH":iospath1234[0],
                "UPTIME":Uptime[0],
                "CONFIG_REGISTER":configregister1234[0]
            })

print("EXCEL IS SUCCESSFULLY GENERATED")



