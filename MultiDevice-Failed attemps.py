from netmiko import ConnectHandler
from netmiko.ssh_exception import NetmikoAuthenticationException
from getpass import getpass
import difflib

multidevice=['192.168.100.220','192.168.100.230','192.168.100.221']

for singledevice in multidevice:
    a=1
    while a <= 5:
        try:
            devicesinfo={
                    "ip": singledevice,
                    'username': "admin",
                    "password": input("Enter the password:"+ singledevice),
                    "device_type": "cisco_ios",
                }

            ssh123 = ConnectHandler(**devicesinfo)
            out123 = ssh123.find_prompt()
            if ">" or "#" in out123:
                print("Login is successfull"  +singledevice)
                out123 = ssh123.find_prompt()
                if ">" or "#" in out123:
                    print(" logging is succesful " + singledevice)
                    config123 = ssh123.send_config_set(["interface lo 101"])
                    # prechecks
                    cmd123 = ["show vlan 150", "show run int lo101", "show run | sec ospf", "show run int lo110"]
                    for singlecmd123 in cmd123:
                        pre123 = ssh123.send_command(singlecmd123)
                        pre123file = open(r"C:\Users\younus\Desktop\python scripts\Logfiles\precheck-" + singledevice + ".txt",
                            "a")
                        copycontent1 = pre123file.write("output for " + singlecmd123 + "\n")
                        copycontent1 = pre123file.write(pre123 + "\n")
                        readcontent1 = open(r"C:\Users\younus\Desktop\python scripts\Logfiles\precheck-" + singledevice + ".txt").readlines()
                    # config changes
                    config123 = ssh123.send_config_set(["no vlan 150", 'int lo101', "router ospf 100", "no int lo101"])
                    # postchecks
                    cmd1234 = ["show vlan 150", "show run int lo101", "show run | sec ospf", "show run int lo110"]
                    for singlecmd1234 in cmd1234:
                        post1234 = ssh123.send_command(singlecmd1234)
                        post123file = open(r"C:\Users\younus\Desktop\python scripts\Logfiles\postcheck-" + singledevice + ".txt",
                            "a")
                        postcopycontent1 = post123file.write("output for " + singlecmd1234 + "\n")
                        postcopycontent1 = post123file.write(post1234 + "\n")
                        readcontent2 = open(r"C:\Users\younus\Desktop\python scripts\Logfiles\postcheck-" + singledevice + ".txt").readlines()
                    # generate html
                    diff123 = difflib.HtmlDiff().make_file(readcontent1, readcontent2, copycontent1, postcopycontent1)
                    make_report = open(r"C:\Users\younus\Desktop\python scripts\Logfiles\diff_report_" + singledevice + ".html",
                        "w")
                    copytoreport = make_report.write(diff123)
                    make_report.close()
                    print("DIFF REPORT GENERATED")

                break
            else:
                pass
        except NetmikoAuthenticationException:
            print("try another time")
            if a==4:
                logs = open(r"C:\Users\younus\Desktop\python scripts\Logfiles\failed_" + ".txt","a")
                copydevices = logs.write(singledevice + "\n")
                logs.close()
        a = a + 1
        print(a)
print("JOB IS DONE")






