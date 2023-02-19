# input any positive integer to output the following calculation.
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.
# author: John Kelleher

# function to calculate new value based on current value (x)
def calculate (x):
    if (x % 2) == 0:
        # value if even
        new_value = x // 2
    else:
        # value if odd
        new_value = (x*3)+1
    return new_value

x = int(input("Input an integer: "))

# extra code to show the steps in the calculation
step = 1
# confirm input with user
print (f"Integer is {x}")

# trying to use is.digit and isinstance for error handling
# https://favtutor.com/blogs/check-string-is-integer-python#:~:text=The%20isdigit()%20method%20is,and%20False%20if%20it's%20not.
# https://www.programiz.com/python-programming/methods/built-in/type
# https://www.digitalocean.com/community/tutorials/python-type

#   if not(isinstance(x,int)):
    #   print ("False")
#   else:    
    #   print ("True")
    
    #   if x.isdigit ():
while x > 1:
    x = calculate (x)
    print (f"Step {step}: {x}")
    step = step+1
    
print (f"The value of our integer is now {x}")

# else:
    # print (f"Please enter an integer.  {x} is not an integer")


