import re
from netmiko import ConnectHandler
Device = {
        "device_type": "paloalto_panos",
        "ip": "192.168.100.200",
        "username": "admin",
        'password': "admin123",
}
ssh123 = ConnectHandler(**Device)

# ******Find Source Zone address given the Source ip address *********

sourceips = open(r"E:\Network Automation\sourceips.txt",)
sourciplist = sourceips.read().splitlines()
for ip in sourciplist:
        Command = "test routing fib-lookup virtual-router Tahakom-VR ip "+ip
        Apply1 = ssh123.send_command(Command)
        regexout = re.compile(r"\s*interface\s*(\S+),")
        output1 = regexout.findall(Apply1)
        print(ip)

        for item in output1:
                Command2 = "show interface "+item
                Apply2 = ssh123.send_command(Command2)
                # print(Apply2)
                regexout1 = re.compile(r"Zone:\s*(\S+),")
                output2 = regexout1.findall(Apply2)
                print(output2[0])
                createlogfile = open(r"E:\Network Automation\sourcezone.txt", "a")
                copycontent123 = createlogfile.write(output2[0] + "\n")
                # copycontent123 = createlogfile.write("\n")
        createlogfile.close()


