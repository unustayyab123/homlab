from datetime import datetime
mytimenow= datetime.now()
# print(mytimenow)

newtimenow=str(mytimenow.year) + "-" + str(mytimenow.month) + "-" + str(mytimenow.day)
print(newtimenow)