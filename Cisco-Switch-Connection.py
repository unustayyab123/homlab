from netmiko import ConnectHandler
# for device in listofdevices:
devicesinfo = {
"ip": ' 192.168.100.220',
'username': 'admin',
"password": 'admin',
"device_type" : "cisco_ios"
}
ssh123 = ConnectHandler(**devicesinfo)
vlans =["Edge-Stag-Prxy" ,"Edge-Sta-MNode" ,"Edge-Sta-WNodes"]
vlan_num = ['1189', '1190', '1191']
vlan_num1 = ['1189']

Configcmd = ["config t", "vlan" , "description"]
config123 = ssh123.send_config_set(Configcmd)

# for number in vlan_num:
#         for name1 in vlans:
#                 names = ["name " + name1]
#                 # config123 = ssh123.send_config_set(cmds)
#         ssh123 = ConnectHandler(**devicesinfo)
#         cmds = ["vlan  " + number +"\n","name "+names[0-2]]
#         cmds123 = ['interface range Ethernet' " 1/1/1/-1/1/2 ",
#                    "switchport trunk allowed vlan " + listed + ",1189-1193"]
#         config123 = ssh123.send_config_set('interface range Ethernet 1/1/1/-1/1/2')
#         config123 = ssh123.send_config_set(cmds)
#         print(config123)


ssh123 = ConnectHandler(**devicesinfo)
# cmds123 = ['interface range Ethernet' " 1/1/1/-1/1/2 ",
#            "switchport trunk allowed vlan " + listed + ",1189-1193"]
cmds =['int range fastEthernet2/0 - 5', 'no shut']
config123 = ssh123.send_config_set(cmds)
# config123 = ssh123.send_config_set(cmds)
print(config123)

