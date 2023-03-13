import time
start = time.time()
from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config,netmiko_file_transfer,netmiko_send_command,netmiko_send_config
from nornir_utils.plugins.functions import print_result

# import logging
# logging.basicConfig(filename='nornir1.log', level=logging.DEBUG)
# logger = logging.getLogger("nornir")

nr123 = InitNornir("21config.yml")
# output123 = nr123.run(netmiko_send_command, command_string="show ip int br")
# output123 = nr123.run(netmiko_send_command, command_string="show ip int br")
output123 = nr123.run(netmiko_send_config, config_file= r"C:\Users\younus\Desktop\python scripts\commands.txt")
# output123 = nr123.run(netmiko_send_config config_commands=["show ip int brief","show run | i hostname"])
# output123 = nr123.run(netmiko_file_transfer, source_file="nornir1.log", dest_file="nornir1.log" )
print_result(output123)

end = time.time()
elapstime = end-start
print(elapstime)
#NAPALM

# from nornir import InitNornir
# from nornir_napalm.plugins.tasks import napalm_get, napalm_cli
# from nornir_utils.plugins.functions import print_result
#
# nrconfig123 = InitNornir("21config.yml")
# # outconfig123 = nrconfig123.run(napalm_cli, commands=["show ip int brief"])
# outconfig123 = nrconfig123.run(napalm_get, getters=["get_interfaces"])
# print_result(outconfig123)

#main python script
# import getpass
# from nornir import InitNornir
# from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
# from nornir_utils.plugins.functions import print_result
# nr123 = InitNornir("21config.yml")
# password123 = getpass.getpass()
# nr123.inventory.defaults.password = password123
# #ssh is established all at once
# outconfig123 = nr123.run(netmiko_send_command, command_string="show ip int br")
# print_result(outconfig123)

#SPEED TEST
