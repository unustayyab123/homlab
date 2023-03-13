from netmiko import ConnectHandler, file_transfer
# import logging
# logging.basicConfig(filename='ospflogging1.log', level=logging.DEBUG)
# logger = logging.getLogger("netmiko")

multidevice = open(r"C:\Users\younus\Desktop\python scripts\devicename.txt", )
listofdevices = multidevice.read().splitlines()

devicetype = open(r"C:\Users\younus\Desktop\python scripts\devicetype.txt", )
devicetypes = devicetype.read().splitlines()
# print(devicetypes)
for device in listofdevices:
    devicetypes =str(input("Enter Device type"))

    devicesinfo = {
    'ip': listofdevices,
    'username': 'admin',
    'password': 'cisco',
    'device_type': devicetypes
    }
    # input123 = input("enter Device type")
    #

    ssh123 = ConnectHandler(**devicesinfo)
    print("ssh established ")
    # else:
    # #    'device_types'==devicetypes[1]
    #     print('hello')

    # elif 'arista_eos' in devicetypes:
    #     ssh123 = ConnectHandler(**devicesinfo)    #     print("Device is arista ---ssh not  established", ssh123)
# else:
#     print("Nothing is found")
# # ssh123 = ConnectHandler(**devicesinfo)
    # if typeofdevice =="cisco_ios":
    # filetransfer123=file_transfer(ssh123,source_file=r"C:\Users\younus\Desktop\python scripts\Logfiles\test.txt",dest_file=r"new.txt",file_system="disk0:",direction="put")
    # else:
    #     filetransfer123 = file_transfer(ssh123, source_file=r"C:\Users\younus\Desktop\python scripts\Logfiles\test.txt",
    #     dest_file=r"new.txt", file_system="/mnt/flash", direction="put")