# this program reads two integer amounts and add them together to create an amount in currency format.
amount1 = int(input ("Enter Amount 1 (in cents): "))
amount2 = int(input ("Enter Amount 1 (in cents): "))
print ("Thank you.  Calculating...")
total = amount1 + amount2

#parse cent amount to euro and cent
euroTotal = ((total)/100)

#specify decimal places for euroTotal
#https://www.freecodecamp.org/news/2f-in-python-what-does-it-mean/#:~:text=In%20Python%2C%20there%20are%20various,point%20number%20is%20rounded%20up.

decimalplace = "%.2f" % euroTotal
#output amount in human readable form
print ("The sum of these is " + "€" + str(decimalplace))

