import netmiko
from netmiko import ConnectHandler
Device = {
        "device_type": "f5_linux",
        "ip": "192.168.100.170",
        "username": "admin",
        'password': "admin123",
}
tms1= "tmsh \n"
tms2= "list /sys management-ip"
ssh123 = ConnectHandler(**Device)
print("successful login ! " + Device["ip"])
fetch123 = ssh123.send_config_set(tms1)
fetch1234 = ssh123.send_command(tms2)
print(fetch1234)
