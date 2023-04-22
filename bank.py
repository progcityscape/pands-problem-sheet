# this program reads two integer amounts and add them together to create an amount in currency format.
'''
from decimal import *
'''
amount1 = int(input ("Enter Amount 1 (in cents): "))
amount2 = int(input ("Enter Amount 1 (in cents): "))
print ("Thank you.  Calculating...")
total = amount1 + amount2
#parse cent amount to euro and cent
euroTotal = ((total)/100)
'''
euroTotal = decimal(total)
'''
#specify decimal places for euroTotal
#https://www.freecodecamp.org/news/2f-in-python-what-does-it-mean/#:~:text=In%20Python%2C%20there%20are%20various,point%20number%20is%20rounded%20up.
print (euroTotal)
decimalplace = "%.2f" % euroTotal
#output amount in human readable form
print ("The sum of these is " + "€" + str(decimalplace))
# still searching for solution that doesn't use float
# unable to use decimal function when I import decimal

