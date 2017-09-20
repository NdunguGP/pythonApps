import datetime

print("-------------------------------------------------")
print("               BIRTHDAY APP ")
print("-------------------------------------------------")

year = int(input("what year were you born [yyyy]"))
month = int(input("what month were you born [MM]"))
dd = int(input("what day were you born [DD]"))

today = str(datetime.date.today())

currentYear = int(today[:4])

birthday = currentYear - year

print("")
print("it looks like you were born on {} / {} / {} ".format(dd, month, year) )
print("looks like your birthday is in {} days".format(birthday))
print("Hope you are looking forward to it!")
