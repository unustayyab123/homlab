
from netmiko import ConnectHandler
Device = {
        "device_type": "paloalto_panos",
        "ip": "192.168.100.200",
        "username": "admin",
        'password': "admin123",
}
ssh123 = ConnectHandler(**Device)

POLICY_NAME = 'Test-Service-port'

tcp_ports = ["TCP-445", "TCP-500", "TCP-540", "TCP-544", "TCP-567"]
serviceport_tcp_list = ["445","446","500"]

for item in serviceport_tcp_list:
    matching = [s for s in tcp_ports if item in s]
    if matching !=[]:
        match2 = matching[0]
        sourceportcommand = "set rulebase security rules "+ POLICY_NAME +" service "  + match2
        fetch123 = ssh123.send_config_set(sourceportcommand)
        print(fetch123)
    else:
        print("no matching found")
        port = "TCP-"+item
        command1 = "set service "+port + " protocol tcp port "+ item
        fetch1 = ssh123.send_config_set(command1)
        print(fetch1)
        command2 = "set rulebase security rules "+ POLICY_NAME +" service " + port
        fetch2 = ssh123.send_config_set(command2)
        print(fetch2)
