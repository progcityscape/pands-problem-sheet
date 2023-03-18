# import datetime module
# https://docs.python.org/3/library/datetime.html#datetime.datetime.weekday
from datetime import datetime

# get current datetime
dt = datetime.now()

# get day of week as integer

current_day = dt.weekday()

# create a list with the days of the week
# not needed for this program

#   today = input ("What day is it today?")
#   weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
#   weekend_days = ["Saturday", "Sunday"]

# iterate through the list of weekdays
# https://stackoverflow.com/questions/42316425/checking-if-a-word-is-in-a-list-in-python
# use a function to do this
# this block (next 8 lines) will be useful in the future but not needed in this program - commented out

#   def check (word, list):
#       if word in list:
#           print ("Yes, unfortunately today is a weekday")
#       else:
#           print ("It is the weekend, yay!")

# check (today, weekdays)

# create function to check day of week as an integer to see if weekend or weekday

def check_day (day):
    if day <=1:
        print ("It is the weekend, yay!")
    else:
        print ("Yes, unfortunately today is a weekday")
    return

check_day (current_day)

# would be easy to assume that this works, however the nature of the program means you are likely to be creating it on one single day, therefore the dt.weekday command will only return one value
# I would implement a test function to check that the integers from 1 - 6 return the desired results 

check_day_test = 0

for check_day_test in range (7):
    print ("checking day of week integers...")
    check_day(check_day_test)
    check_day_test += 1

if check_day_test > 6:
    print ("finished checking.")







