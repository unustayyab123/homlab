import netmiko
import json
import creds
import logging
logging.basicConfig(filename='palo4.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")
from netmiko import ConnectHandler
Device = {
        "device_type": "paloalto_panos",
        "ip": "192.168.100.200",
        "username": "admin",
        'password': "admin123",
}
ssh123 = ConnectHandler(**Device)

#PALO ALTO SHOW COMMANDS SAMPLE SCRIPT
#print("successful login ! " + Device["ip"])
# palocommandslist = open(r"C:\Users\younus\Desktop\python scripts\palo-commands.txt", )
# palocommands = palocommandslist .read().splitlines()
#
# for commands in palocommands:
#         fetch1234 = ssh123.send_command(commands)
#         print(fetch1234)

list1 = 'show service | match "tcp port 8080"'
fetch1234 = ssh123.send_config_set(list1)
# out123=json.dumps(fetch1234,sort_keys="True",indent=4)
print(fetch1234)

#PALO ALTO CONFIG COMMANDS SAMPLE SCRIPT
# config1= "configure \n"
#config2="set rulebase security rules test-config from Internet to Intranet destination any application any service any action allow \n"
# config3 = "set rulebase security rules TEST source 192.168.1.1 192.168.1.2 192.168.1.3 192.168.1.4 \n"
# source="set rulebase security rules source2 source [ 192.168.3.1 192.168.4.5 192.168.6.6 192.168.6.6 ] \n"
# sourceinput=ssh123.send_command(source)
# destination="set rulebase security rules source2 destination [ 192.168.5.1 192.168.9.5 192.168.10.6 192.168.100.6 ] \n"
# destinationinput=ssh123.send_command(destination)
# user="set rulebase security rules source2 source-user [ 'tahakom\\unus1' ' tahakom\\unus4 '] \n"
# userinput = ssh123.send_command(user)
# action = "set rulebase security rules source2 action allow \n"
# actioninput = ssh123.send_command(action)
# sourcezone ="set rulebase security rules source2 from [ Intranet test2 ] \n"
# sourcezoneinput= ssh123.send_config_set(sourcezone)
# destzone ="set rulebase security rules source2 to [ Internet test2 ] \n"
# Destzoneinput = ssh123.send_config_set(destzone)
# application ="set rulebase security rules source2 application any \n"
# applicationinput = ssh123.send_config_set(application)
# service ="set rulebase security rules source2 service any \n"
# serviceinput = ssh123.send_config_set(service)
# # commit = "commit \n"
# # fetch123 = ssh123.send_config_set(commit)
# print("config done")