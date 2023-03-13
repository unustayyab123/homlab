
import netmiko
# import json
import logging
logging.basicConfig(filename='console.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")
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

#********IDM RULES---VLANS TO IDM***************
# Source subnet
sourcesubnet = "set rulebase security rules ALL_VLANS_to_IDM  source 10.172.50.0_24  \n"
sourceinput=ssh123.send_config_set(sourcesubnet)
# Source zone
sourcezone ="set rulebase security rules ALL_VLANS_to_IDM  from [ servicenow-int-Prod-UI servicenow-int-Prod-Wrkr servicenow-int-Prod-DB  servicenow-Ext-Prod-UI ] \n"
sourcezoneinput= ssh123.send_config_set(sourcezone)
print("IDM--Source subnet and Source Zone Added")
#********IDM RULES---IDM to VLANS **************
# Destination subnet
destinationsubnet = "set rulebase security rules IDM-to-ALL_VLANS  destination 10.172.50.0_24  \n"
destinationinput=ssh123.send_config_set(destinationsubnet)
# Destination zone
destinationzone ="set rulebase security rules IDM-to-ALL_VLANS  to [ servicenow-int-Prod-UI servicenow-int-Prod-Wrkr servicenow-int-Prod-DB  servicenow-Ext-Prod-UI ] \n"
destinationzoneinput= ssh123.send_config_set(destinationzone)
print("IDM--Destination subnet and Dest Zone Added")

#********NTP RULES---VLANS TO NTP***************
# Source subnet
sourcesubnet = "set rulebase security rules ALL_VLANS_to_NTP  source 10.172.50.0_24  \n"
sourceinput=ssh123.send_config_set(sourcesubnet)
# Source zone
sourcezone ="set rulebase security rules ALL_VLANS_to_NTP  from [ servicenow-int-Prod-UI servicenow-int-Prod-Wrkr servicenow-int-Prod-DB  servicenow-Ext-Prod-UI ] \n"
sourcezoneinput= ssh123.send_config_set(sourcezone)
print("NTP--Source subnet and Source Zone Added")

#********SATELITE SERVER RULES---VLANS TO SATELITE***************
# Source subnet
sourcesubnet = "set rulebase security rules ALL_VLANS_to_Satellite  source 10.172.50.0_24  \n"
sourceinput=ssh123.send_config_set(sourcesubnet)
# Source zone
sourcezone ="set rulebase security rules ALL_VLANS_to_Satellite  from [ servicenow-int-Prod-UI servicenow-int-Prod-Wrkr servicenow-int-Prod-DB  servicenow-Ext-Prod-UI ] \n"
sourcezoneinput= ssh123.send_config_set(sourcezone)
print("SATELITE SERVER--Source subnet and Source Zone Added")
#********SATELITE SERVER RULES---SATELITE to VLANS **************
# Destination subnet
destinationsubnet = "set rulebase security rules Satellite_to_ALL_VLANS  destination 10.172.50.0_24  \n"
destinationinput=ssh123.send_config_set(destinationsubnet)
# Destination zone
destinationzone ="set rulebase security rules Satellite_to_ALL_VLANS  to [ servicenow-int-Prod-UI servicenow-int-Prod-Wrkr servicenow-int-Prod-DB  servicenow-Ext-Prod-UI ] \n"
destinationzoneinput= ssh123.send_config_set(destinationzone)
print("SATELITE SERVER--Destination subnet and Dest Zone Added")

#********DNS SERVER RULES---VLANS TO DNS***************
# Source subnet
sourcesubnet = "set rulebase security rules ALL_VLANS_to_AD_DNS  source 10.172.50.0_24  \n"
sourceinput=ssh123.send_config_set(sourcesubnet)
# Source zone
sourcezone ="set rulebase security rules ALL_VLANS_to_AD_DNS  from [ servicenow-int-Prod-UI servicenow-int-Prod-Wrkr servicenow-int-Prod-DB  servicenow-Ext-Prod-UI ] \n"
sourcezoneinput= ssh123.send_config_set(sourcezone)
print("DNS SERVER--Source subnet and Source Zone Added")
#********DNS SERVER RULES---DNS to VLANS **************
# Destination subnet
destinationsubnet = "set rulebase security rules AD_DNS_to_ALL_VLANS  destination 10.172.50.0_24  \n"
destinationinput=ssh123.send_config_set(destinationsubnet)
# Destination zone
destinationzone ="set rulebase security rules AD_DNS_to_ALL_VLANS  to [ servicenow-int-Prod-UI servicenow-int-Prod-Wrkr servicenow-int-Prod-DB  servicenow-Ext-Prod-UI ] \n"
destinationzoneinput= ssh123.send_config_set(destinationzone)
print("DNS SERVER--Destination subnet and Dest Zone Added")

# #********WSUS SERVER RULES---VLANS TO WSUS***************
# # Source subnet
sourcesubnet = "set rulebase security rules ALL_VLANS_to_WSUS  source 10.172.50.0_24  \n"
sourceinput=ssh123.send_config_set(sourcesubnet)
# Source zone
sourcezone ="set rulebase security rules ALL_VLANS_to_WSUS  from [ servicenow-int-Prod-UI servicenow-int-Prod-Wrkr servicenow-int-Prod-DB  servicenow-Ext-Prod-UI ] \n"
sourcezoneinput= ssh123.send_config_set(sourcezone)
print("WSUS SERVER--Source subnet and Source Zone Added")
#********WSUS SERVER RULES---WSUS to VLANS **************
# Destination subnet
destinationsubnet = "set rulebase security rules WSUS_to_ALL_VLANS  destination 10.172.50.0_24  \n"
destinationinput=ssh123.send_config_set(destinationsubnet)
# Destination zone
destinationzone ="set rulebase security rules WSUS_to_ALL_VLANS  to [ servicenow-int-Prod-UI servicenow-int-Prod-Wrkr servicenow-int-Prod-DB  servicenow-Ext-Prod-UI ] \n"
destinationzoneinput= ssh123.send_config_set(destinationzone)
print("WSUS SERVER--Destination subnet and Dest Zone Added")