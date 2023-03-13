#netmiko
from netmiko import ConnectHandler
opendevicelist = open(r"C:\Users\younus\Desktop\python scripts\devicename.txt")
readdevicelist = opendevicelist.read().splitlines()
print(readdevicelist)

opencredfile = open(r"C:\Users\younus\Desktop\python scripts\devicecred.txt")
readcred = opencredfile.read().splitlines()

#print(readcred)
user1 = readcred[0]
print(user1)
pass1 = readcred[1]
print(pass1)
# secr1 = readcred[2]
# print(secr1)
for singledcv in readdevicelist:
    deviceinfo123 = {
        "ip": singledcv,
        "username": user1,
        "password": pass1,
        "device_type": "cisco_ios"
    }
    ssh123 = ConnectHandler(**deviceinfo123)
    print("**"*5 + " Connected to " + singledcv)
    intid = input("enter the interface id: ")
    output1 = ssh123.send_command("show interface " + intid).splitlines()[0]
    print(output1)
    if "up" and "up" in output1:
        print("no action required")
    elif "down" and "down" in output1:
        print("bringing up the interface")
        bringup1 = ssh123.send_config_set(["inter " + intid, "no shutdown", "desc **reserved for CR1234"])
        print(bringup1)
    ssh123.disconnect()

