# Still working on this...

# read in a 10 character account number and output just the last 4 digits
#format xxxxxxyyyy

#create a function to truncate the account number to last 4 digits


# create a program that will handle account numbers of any size.  
# Assuming that this means we will take the last four digits and add a number of x's before them.
# The number of x's could be the length of the string (excluding last 4 digits)
# Also assuming that the account number will be at least 4 digits long

# Create a new function that returns the length of the inputted account number.  

def account_no_length (x):
    no_of_digits = len (x)
    return int(no_of_digits)


# alter the sixchar function to deal with new account length

def sixchar_long (x):
    string_trun = x [len(x)-6:len(x)]
    return string_trun


# now repeat previous steps but add in new functions

# read in 10 digit account number

account_no = input("Please enter an account number: ")


# assign the outputs of the new functions to variables

long_account_length = account_no_length (account_no)


# assign sixchar function output to variable
string_trun = sixchar_long(account_no)

# alter the 'convert' function to adjust for the new account length where y is the account no. length

def convert_x (y):
    no_of_xs = len(y)-6
    
    # repeat x the required number of times
    # https://linuxhint.com/how-do-you-repeat-a-string-n-times-in-python/#:~:text=In%20Python%2C%20we%20utilize%20the,by%20a%20%E2%80%9C*%E2%80%9D%20sign.

    wildcards = "x"*no_of_xs

    return wildcards

# create final account number with x's added

final_number_new = convert_x (account_no) + string_trun
print (final_number_new)












