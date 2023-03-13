import re
from netmiko import ConnectHandler
Device = {
        "device_type": "paloalto_panos",
        "ip": "192.168.100.200",
        "username": "admin",
        'password': "admin123",
}
ssh123 = ConnectHandler(**Device)

POLICY_NAME = 'Test-Service-port'

tcp_ports = ["TCP-445", "TCP-500", "TCP-540", "TCP-544", "TCP-567"]
serviceport_tcp_list = ["445","446","500"]

for item in serviceport_tcp_list:
    matching = [s for s in tcp_ports if item in s]
    if matching !=[]:
        match2 = matching[0]
        sourceportcommand = "set rulebase security rules source17 service " + match2
        fetch123 = ssh123.send_config_set(sourceportcommand)
        print(match2)
    else:
        print("no matching found")

# ******Find Service Port *********
# test = "set cli config-output-format set \n"
# Apply1 = ssh123.send_command(test)
# test3 = 'show service | match "protocol tcp port " \n'
# Apply3 = ssh123.send_config_set(test3)
# regexout = re.compile(r"\s*service\s*(.\S+)")
# tcp_ports = regexout.findall(Apply3)
# # print(tcp_ports)

# sourceport1 = open(r"E:\Network Automation\sourceport.txt",)
# sourceportlist = sourceport1.read().splitlines()
# print(sourceportlist)

# for item in sourceportlist:
#     if item in tcp_ports:
#         matching = [s for s in tcp_ports if item in s]
#         match2 = matching[0]
#         print(match2)

    # else:
    #     print(" item not in list")
#
# from netmiko import ConnectHandler
# Device = {
#         "device_type": "paloalto_panos",
#         "ip": "10.175.0.60",
#         "username": "admin",
#         'password': "test1243",
#}


