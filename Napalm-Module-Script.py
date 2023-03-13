#Napalm
import json
# from napalm import get_network_driver
# driver123=get_network_driver("ios")
# ios123=driver123("192.168.100.230","admin","cisco")
# ios123.open()
# #ssh Established
# output123=ios123.get_config()["running"]
# # out123=json.dumps(output123,sort_keys=True,indent=4)
# print(output123)

import json
from napalm import get_network_driver
driver123=get_network_driver("ios")
ios123=driver123("192.168.100.221","admin","cisco")
ios123.open()
ios123.load_merge_candidate(r"C:\Users\younus\Desktop\python scripts\Logfiles\config.txt")
diff123 = ios123.compare_config()
print(diff123)
# if len(diff123):
#     answer123 = input("yes ? No")
#     if answer123 == "yes":
#         print("perform the change")
#         ios123.commit_config()
#         print("change applied successfully")
#     else:
#         print("Config Declined by user")
# ios123.close()


