import netmiko
import re
from netmiko import ConnectHandler
Device = {
        "device_type": "paloalto_panos",
        "ip": "192.168.100.200",
        "username": "admin",
        'password': "admin123",
}
ssh123 = ConnectHandler(**Device)
#POLICY NAME
POLICY_NAME ='Policy-Test-All-New1'

##SOURCE IP LIST
Sourceip = open(r"E:\Network Automation\sourceips-1.txt")
Sourceip_LIST = Sourceip.read().splitlines()

for name in Sourceip_LIST:
        source_ips = ssh123.send_config_set( "set rulebase security rules " + POLICY_NAME + " source " + name)
        print(source_ips)
print("Source IPS Added to "+ POLICY_NAME)

##******Find Source Zone from Sourceip_LIST *********
for ip in Sourceip_LIST:
        Command = "test routing fib-lookup virtual-router Tahakom-VR ip "+ip
        interfacecommand = ssh123.send_command_timing(Command)
        regexout = re.compile(r"\s*interface\s*(\S+),")
        interfaces = regexout.findall(interfacecommand)
        print(ip)

        for interface in interfaces:
                Command2 = "show interface "+interface
                Apply2 = ssh123.send_command_timing(Command2)
                # print(Apply2)
                regexout1 = re.compile(r"Zone:\s*(.+),")
                Zonelist = regexout1.findall(Apply2)
                print(Zonelist)
                createlogfile = open(r"E:\Network Automation\sourcezone.txt", "a")
                copycontent123 = createlogfile.write(Zonelist[0] + "\n")
        # copycontent123 = createlogfile.write("\n")
        createlogfile.close()
# ssh123.disconnect()

##ADDING SOURCE ZONES TO POLICY
Source_zone = open(r"E:\Network Automation\sourcezone.txt")
SrcZone_LIST = Source_zone .read().splitlines()
for zone in SrcZone_LIST:
    SourceZone = ssh123.send_config_set("set rulebase security rules "+ POLICY_NAME + " from " + zone)
print("Source Zone Added to "+ POLICY_NAME)


#DESTINATION IP LIST
destination_ip = open(r"E:\Network Automation\destination-ips-1.txt")
destination_ip_LIST = destination_ip.read().splitlines()

for name in destination_ip_LIST:
    dest_ips = ssh123.send_config_set("set rulebase security rules "+ POLICY_NAME + " destination " + name)
    print(dest_ips)
print("Destination IPS Added to "+ POLICY_NAME)

##******Find Dest Zone from destination_ip_LIST *********
for ip in destination_ip_LIST:
        Command = "test routing fib-lookup virtual-router Tahakom-VR ip "+ip
        interfacecommand = ssh123.send_command_timing(Command)
        regexout = re.compile(r"\s*interface\s*(\S+),")
        interfaces = regexout.findall(interfacecommand)
        print(ip)

        for interface in interfaces:
                Command2 = "show interface "+interface
                Apply2 = ssh123.send_command_timing(Command2)
                # print(Apply2)
                regexout1 = re.compile(r"Zone:\s*(.+),")
                Zonelist = regexout1.findall(Apply2)
                # print(Zonelist)
                createlogfile = open(r"E:\Network Automation\destinationzone.txt", "a")
                copycontent123 = createlogfile.write(Zonelist[0] + "\n")
        #copycontent123 = createlogfile.write("\n")
        createlogfile.close()

#ADDING DEST ZONES TO POLICY
Destination_zone = open(r"E:\Network Automation\destinationzone.txt")
DESTZone_LIST = Destination_zone .read().splitlines()
for zone in DESTZone_LIST:
    DestZone = ssh123.send_config_set("set rulebase security rules "+ POLICY_NAME + " to " + zone)
print("Destination Zone Added to " + POLICY_NAME)

#******Find TCP--Service Port *********
test = "set cli config-output-format set \n"
Apply1 = ssh123.send_command(test)
test3 = 'show service | match "protocol tcp port " \n'
Apply3 = ssh123.send_config_set(test3)
regexout = re.compile(r"\s*service\s*(.\S+)")
tcp_ports = regexout.findall(Apply3)
#
for port in tcp_ports:
    serviceport = open(r"E:\Network Automation\tcp-port-DC-FW.txt","a")
    serviceports_list = serviceport.write(port + "\n")
    serviceport.close()
## ***ADDING TCP-Service Ports ******
tcp_ports_list = open(r"E:\Network Automation\tcp-port-DC-FW.txt")
tcp_ports = tcp_ports_list.read().splitlines()

serviceport_tcp = open(r"E:\Network Automation\serviceport-tcp.txt",)
serviceport_tcp_list = serviceport_tcp.read().splitlines()
# print(sourceportlist)

for item in serviceport_tcp_list:
    matching = [s for s in tcp_ports if item in s]
    if matching !=[]:
        match2 = matching[0]
        sourceportcommand = "set rulebase security rules "+ POLICY_NAME +" service " + match2
        fetch123 = ssh123.send_config_set(sourceportcommand)
        print(fetch123)
    else:
        print("no matching found")
        port = "TCP-"+item
        command1 = "set service "+port + " protocol tcp port "+ item
        fetch1 = ssh123.send_config_set(command1)
        print(fetch1)
        command2 = "set rulebase security rules "+ POLICY_NAME +" service " + port
        fetch2 = ssh123.send_config_set(command2)
        print(fetch2)

#******Find UDP--Service Port *********
# test = "set cli config-output-format set \n"
# Apply1 = ssh123.send_command(test)
# test4 = 'show service | match "protocol udp port " \n'
# Apply4 = ssh123.send_config_set(test4)
# regexout1 = re.compile(r"\s*service\s*(.\S+)")
# udp_ports = regexout1.findall(Apply4)
# for port in udp_ports:
#     serviceport1 = open(r"E:\Network Automation\UDP-port-DC-FW.txt","a")
#     serviceports1_list = serviceport1.write(port + "\n")
#     serviceport1.close()

## ***ADDING UDP-Service Ports ******
# udp_ports_list = open(r"E:\Network Automation\UDP-port-DC-FW.txt")
# udp_ports = udp_ports_list.read().splitlines()
#
# serviceport_udp = open(r"E:\Network Automation\serviceport-udp.txt",)
# serviceport_udp_list = serviceport_tcp.read().splitlines()
#
# for item in serviceport_udp_list:
#     matching = [s for s in udp_ports if item in s]
#     if matching !=[]:
#         match2 = matching[0]
#         sourceportcommand = "set rulebase security rules "+ POLICY_NAME +" service "  + match2
#         fetch123 = ssh123.send_config_set(sourceportcommand)
#         print(fetch123)
#     else:
#         print("no matching found")
#         port = "UDP-"+item
#         command1 = "set service "+port + " protocol tcp port "+ item
#         fetch1 = ssh123.send_config_set(command1)
#         print(fetch1)
#         command2 = "set rulebase security rules "+ POLICY_NAME +" service " + port
#         fetch2 = ssh123.send_config_set(command2)
#         print(fetch2)

#COMMON TO ALL POLICIES
Action = ssh123.send_config_set("set rulebase security rules " +POLICY_NAME+ " action allow \n")
application = ssh123.send_config_set("set rulebase security rules " +POLICY_NAME+" application any \n")
# log_forwarding = ssh123.send_config_set("set rulebase security rules " + POLICY_NAME + " log-setting LogRhythm_Syslog")
# profile_setting = ssh123.send_config_set("set rulebase security rules " + POLICY_NAME + " profile-setting group SCAN_GRP")

print("POLICY "+POLICY_NAME+" CREATED SUCCESSFULLY")