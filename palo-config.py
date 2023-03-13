import re
from netmiko import ConnectHandler
Device = {
        "device_type": "paloalto_panos",
        "ip": "192.168.100.200",
        "username": "admin",
        'password': "admin123",
}
ssh123 = ConnectHandler(**Device)
#***Source ip address **************
sourceip = open(r"E:\Network Automation\paloconfig\sourceip.txt", )
sourceiplist = sourceip.read().splitlines()

for ip in sourceiplist:
        source = "set rulebase security rules palo-config source " + ip
        fetch123 = ssh123.send_config_set(source)

#***Destintion ip address **************
destinationip = open(r"E:\Network Automation\paloconfig\destinatonip.txt", )
destioniplist = destinationip.read().splitlines()

for ip in destioniplist:
        destip ="set rulebase security rules palo-config destination " + ip
        fetch123 = ssh123.send_config_set(destip)

#*********APPLICATION*****************
application ="set rulebase security rules palo-config application any \n"
applicationinput = ssh123.send_config_set(application)

#*********ACTION*****************
action = "set rulebase security rules palo-config action allow \n"
actioninput = ssh123.send_command(action)
print("Config DONE")

#********** SOURCE-DESTINATION ZONE *********
# sourcezone ="set rulebase security rules palo-config from [ Intranet test2 ] \n"
# sourcezoneinput= ssh123.send_config_set(sourcezone)
# destzone ="set rulebase security rules palo-config to [ Internet test2 ] \n"
# Destzoneinput = ssh123.send_config_set(destzone)