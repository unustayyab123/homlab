import netmiko
import json
import logging
logging.basicConfig(filename='palo6.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")
from netmiko import ConnectHandler
Device = {
        "device_type": "paloalto_panos",
        "ip": "192.168.100.200",
        "username": "admin",
        'password': "admin123",
}
ssh123 = ConnectHandler(**Device)
#CONFIG COMMANDS
source = "set rulebase security rules source2 source [ 192.168.3.1 192.168.4.5 192.168.6.6 192.168.6.6 ] \n"
destination = "set rulebase security rules source2 destination [ 192.168.5.1 192.168.9.5 192.168.10.6 192.168.100.6 ] \n"
user = "set rulebase security rules source2 source-user [ 'tahakom\\unus1' ' tahakom\\unus4 '] \n"
source_zone = "set rulebase security rules source2 from [ Intranet Internet ] \n"
destin_zone = "set rulebase security rules source2 to [ Internet Intranet ] \n"
application_Action = "set rulebase security rules source2 application any action allow \n"
service = "set rulebase security rules source2 service any \n"
# action = "set rulebase security rules source2 action allow \n"

commands = [source, destination, user, source_zone, destin_zone, application_Action, service]
for command in commands:
        Apply = ssh123.send_config_set(command)

print("config done")
# serviceinput = ssh123.send_config_set(service)
# commit = "commit \n"
# fetch123 = ssh123.send_config_set(commit)