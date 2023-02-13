#read in a 10 character account number and output just the last 4 digits
#format xxxxxxyyyy

# author: John Kelleher

#create a function to truncate the account number to last 4 digits

def sixchar (x):
    string_trun = x [6:10]
    return string_trun

#create a function to add a 6 character prefix

def convert ():
    new_no = ("xxxxxx" + string_trun)
    return new_no

# read in 10 digit account number

account_no = input("Please enter a 10 digit account number: ")



# assign sixchar function output to variable
string_trun = sixchar (account_no)

# create final account number with x's added

final_number = convert ()
print (final_number)

# the following section is not working and is explored further in accounts1.2_.py
# create a program that will handle account numbers of any size.  
# Assuming that this means we will take the last four digits and add a number of x's before them.
# The number of x's could be the length of the string (excluding last 4 digits)

# Create a new function that returns the length of the inputted account number.  

def account_no_length (x):
    no_of_digits = len (x)
    return int(no_of_digits)

# alter the 'convert' function to adjust for the new account length where y is the account no. length

def convert_long (y):
    new_no = ("x"*(len(y)-6) + string_strun)
    return new_no


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

# create final account number with x's added

final_number_new = convert_long (string_trun)
print (final_number_new)


## This version is not working - continued in accounts1.2_.py










