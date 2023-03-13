from netmiko import ConnectHandler
Device = {
        "device_type": "paloalto_panos",
        "ip": "192.168.100.200",
        "username": "admin",
        'password': "admin123",
}
ssh123 = ConnectHandler(**Device)

# ******Create New Zone on Malqa DC-FW****

VLAN_list = open(r"E:\Network Automation\vlans-name.txt",)
vlan_Name = VLAN_list.read().splitlines()

for name in vlan_Name:
        Zone_create = ssh123.send_config_set("set zone "+name + " network layer3" )
        print(Zone_create)
        print( "Zone" + name + "created ")