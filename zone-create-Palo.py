# ******Create New Zone on Malqa DC-FW****

from netmiko import ConnectHandler
Device = {
        "device_type": "paloalto_panos",
        "ip": "192.168.100.200",
        "username": "admin",
        'password': "admin123",
}
ssh123 = ConnectHandler(**Device)
##ZONE NAMES
Zone_list = open(r"E:\Network Automation\vlans-name.txt",)
Zone_Name = Zone_list.read().splitlines()

###INTERFACE NUMBER FOR ZONE
INTF_NUMBER = open(r"E:\Network Automation\Zone-Interfaces.txt",)
intf_num = INTF_NUMBER.read().splitlines()

intf_count = print(len(intf_num))

###CREATING ZONES
r=0
while r<len(intf_num):
 for name in Zone_Name:
             ssh123 = ConnectHandler(**Device)
             # cmds123 = ["vlan " + number, "name " + vlan_Name[0+r]]
             Zone_create = ssh123.send_config_set("set zone " + name + " network layer3 " +intf_num[0+r])
             print(Zone_create)
             print("Zone  " + name + "  created Successfully")
             r=r+1
