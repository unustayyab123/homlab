import re
from netmiko import ConnectHandler
Device = {
        "device_type": "paloalto_panos",
        "ip": "10.175.0.60",
        "username": "myounis",
        'password': "Younus$1974",
}
ssh123 = ConnectHandler(**Device)

# ******Find Zone address given the ip address *********

sourceips = open(r"C:\Users\unust\OneDrive\Desktop\Younus\sourceips.txt",)
sourciplist = sourceips.read().splitlines()
for ip in sourciplist:
        Command = "test routing fib-lookup virtual-router default ip "+ip
        interfacecommand = ssh123.send_command(Command)
        regexout = re.compile(r"\s*interface\s*(\S+),")
        interfaces = regexout.findall(interfacecommand)
        print(ip)

        for interface in interfaces:
                Command2 = "show interface "+interface
                Apply2 = ssh123.send_command(Command2)
                # print(Apply2)
                regexout1 = re.compile(r"Zone:\s*(\S+),")
                Zonelist = regexout1.findall(Apply2)
                print(Zonelist[0] ,"\n")
                createlogfile = open(r"C:\Users\unust\OneDrive\Desktop\Younus\sourcezone.txt", "a")
                copycontent123 = createlogfile.write(Zonelist[0] + "\n")
                # copycontent123 = createlogfile.write("\n")
        createlogfile.close