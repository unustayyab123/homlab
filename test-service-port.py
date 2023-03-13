import re
from netmiko import ConnectHandler
Device ={
        "device_type": "paloalto_panos",
        "ip": "192.168.100.200",
        "username": "admin",
        'password': "admin123",
}
ssh123 = ConnectHandler(**Device)
POLICY_NAME ='Test-Service-port'

list1 = ["TCP-445","TCP-500","TCP-540","TCP-544","TCP-567"]
list2= [445,446,500]

for item in list2:
    if item in list1 == True:
        matching = [s for s in list2 if item in s]
        match2 = matching[0]
        print(match2)
        # fetch123 = ssh123.send_config_set("set rulebase security rules " + POLICY_NAME + " service " + match2)
        # print(fetch123)
    else:
        print("no match found")
        # fetch1234 = ssh123.send_config_setset("service test protocol tcp port 123")


