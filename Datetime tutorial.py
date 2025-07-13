# Datetime Tutorial 
import datetime
# To get the current date time


# 1
# now = datetime.datetime.now()
# print(now)
# # 2

# know = datetime.datetime.now()
# print("The time and date is:",know)
# # 3

# some = datetime.datetime.now()

# print("In my local computer The time is:",some)



# To get the input date and time in readable format

# 1

# now =datetime.datetime(2024,9,12,10,25,53)
# print(now)
# # 2

# know =datetime.datetime(2000,3,23)
# print("The past date is: " ,know)
# # 3

# some = datetime.datetime(2030,2,13)

# print ("The time after 6 years is: " ,some)


# To extract everything from date and time
# 1

now = datetime.datetime.now()
print("The current year is:" ,now.strftime("%y")) # note chote wal a-24
print("The current year is: " ,now.strftime("%Y")) #bade wala -2024
# 2
print("The current month is: " ,now.strftime("%m")) # gives the month in number format


# 3
print("The Current minute is:",now.strftime("%M")) # gives the current minute in number format



# 4
print("The current month in letter format is:",now.strftime("%b")) 
print("The current month in full letter format is:",now.strftime("%B"))
# 5
print("The Current hour according to 24 hours is:",now.strftime("%H"))
print("The current hours is:",now.strftime("%F"))

print("The current seconds are :",now.strftime("%S"))
# 6
print("The Current time is:",now.strftime("%H-%M-%S"))

