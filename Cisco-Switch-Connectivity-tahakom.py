from netmiko import ConnectHandler

devicesinfo = {
"ip": ' 192.168.100.220',
'username': 'admin',
"password": 'admin',
"device_type" : "cisco_ios"
}
ssh123 = ConnectHandler(**devicesinfo)
###VLAN NAMES
VLAN_list = open(r"C:\Users\younus\Desktop\python scripts\vlans-name.txt",)
vlan_Name = VLAN_list.read().splitlines()


###VLAN NUMBERS
VLAN_NUMBER = open(r"C:\Users\younus\Desktop\python scripts\vlans-number.txt",)
vlan_num = VLAN_NUMBER.read().splitlines()
vlan_count = print(len(vlan_num))
print(vlan_count)

###CREATING VLANS
r=0
while r<len(vlan_num):
 for number in vlan_num:
             ssh123 = ConnectHandler(**devicesinfo)
             cmds123 = ["vlan " + number, "name " + vlan_Name[0+r]]
             # print(cmds123)
             config123 = ssh123.send_config_set(cmds123,delay_factor=60)
             print(config123)
             r=r+1
# #########ADD VLAN TO  PORT-CHANNEL ###############
vlanrange =vlan_num[0]+"-"+vlan_num[-1]
print(vlanrange)
pchannel_1 = ["int port-channel 1", "switchport trunk allowed vlan add "+vlanrange]
pchannel_2 = ["int port-channel 2", "switchport trunk allowed vlan add "+vlanrange]
config123 = ssh123.send_config_set(pchannel_1)
print(config123)
config123 = ssh123.send_config_set(pchannel_2)
print(config123)
