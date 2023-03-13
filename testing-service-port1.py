import re
from netmiko import ConnectHandler
Device = {
        "device_type": "paloalto_panos",
        "ip": "192.168.100.200",
        "username": "admin",
        'password': "admin123",
}
ssh123 = ConnectHandler(**Device)

# ******Find Service Port *********
# test = "set cli config-output-format set \n"
# Apply1 = ssh123.send_command(test)
# test3 = 'show service | match "protocol tcp port " \n'
# Apply3 = ssh123.send_config_set(test3)
# regexout = re.compile(r"\s*service\s*(.\S+)")
# tcp_ports = regexout.findall(Apply3)
# print(tcp_ports)

sourceport1 = open(r"E:\Network Automation\sourceport.txt",)
sourceportlist = sourceport1.read().splitlines()
# print(sourceportlist)

tcp_port = open(r"E:\Network Automation\destport-HQ-tcp.txt",)
tcp_ports = tcp_port.read().splitlines()
# print(tcp_ports)
##TCP-Port Find
for item in sourceportlist:
        matching = [s for s in tcp_ports if item in s]
        match2 = matching[0]
        print(match2)
        sourceportcommand = "set rulebase security rules source7 service "+ match2
        fetch123 = ssh123.send_config_set(sourceportcommand)
        print(fetch123)

# udp_port = open(r"E:\Network Automation\destport-HQ-udp.txt",)
# udp_ports = udp_port.read().splitlines()
#print(sourceportlist)

##UDP-Port Find
# for item in sourceportlist:
#         matching = [s for s in udp_ports if item in s]
#         match3 = matching[0]
#         # sourceportcommand = "set rulebase security rules source7 service " + match2
#         # fetch123 = ssh123.send_config_set(sourceportcommand)
#         print(match3, "\n")

