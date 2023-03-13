from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config,netmiko_file_transfer,netmiko_send_command
from nornir_utils.plugins.functions import print_result

# import logging
# logging.basicConfig(filename='nornir1.log', level=logging.DEBUG)
# logger = logging.getLogger("nornir")

nr123 = InitNornir("21config.yml")
# output123 = nr123.run(netmiko_send_command, command_string="show ip int br")
output123 = nr123.run(netmiko_send_config,config_commands=["ip scp server enable"])
output123 = nr123.run(netmiko_file_transfer, source_file="nornir1.log", dest_file="nornir1.log" )
print_result(output123)