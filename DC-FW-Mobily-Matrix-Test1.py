
import netmiko
from netmiko import ConnectHandler
Device = {
        "device_type": "paloalto_panos",
        "ip": "192.168.100.200",
        "username": "admin",
        'password': "admin123",
}
ssh123 = ConnectHandler(**Device)
#Define address object to be added
addressobject = "set address 10.172.50.0_24 ip-netmask 10.172.50.0/24 \n"
addresscommand = ssh123.send_config_set(addressobject)

#Rules
Rule1 = ['ALL_VLANS_to_IDM','ALL_VLANS_to_NTP','ALL_VLANS_to_Satellite','ALL_VLANS_to_AD_DNS',
'ALL_VLANS_to_WSUS']

Rule2 = ['IDM-to-ALL_VLANS','Satellite_to_ALL_VLANS','AD_DNS_to_ALL_VLANS','WSUS_to_ALL_VLANS']

# Source subnet and Source Subnet
for Rule in Rule1:
        sourcesubnet = "set rulebase security rules " +Rule+ " source 10.172.50.0_24  \n"
        sourceinput=ssh123.send_config_set(sourcesubnet)
        # print(sourceinput)
        sourcezone = "set rulebase security rules " +Rule+  " from [ servicenow-int-Prod-UI servicenow-int-Prod-Wrkr servicenow-int-Prod-DB  servicenow-Ext-Prod-UI ] \n"
        sourcezoneinput= ssh123.send_config_set(sourcezone)
        # print(sourcezoneinput)
print("Source Subnet and Source Zone Added ")

# Destination subnet and Destination Subnet
for Rule in Rule2:
        destsubnet = "set rulebase security rules " +Rule+ " destination 10.172.50.0_24  \n"
        destinput=ssh123.send_config_set(destsubnet)
        # print(destinput)
        destinputzone = "set rulebase security rules " +Rule+  " to [ servicenow-int-Prod-UI servicenow-int-Prod-Wrkr servicenow-int-Prod-DB  servicenow-Ext-Prod-UI ] \n"
        deszoneinput= ssh123.send_config_set(destinputzone)
        # print(deszoneinput)
print("destination Subnet and destination Zone Added ")

