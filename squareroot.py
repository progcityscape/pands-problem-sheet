# the purpose of this program is to estimate the square root of an input manually (not using pythonm's built in functions).
# to do this we will create a function to estimate the root, based on the Newton Method
# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
# root = 0.5 * (X + (N / X)) where X is any guess which can be assumed to be N or 1.
# Tolerance limit is the maximum difference between X and root allowed. 
# Assign X to the N itself.
# Now, start a loop and keep calculating the root which will surely move towards the correct square root of N.
# Check for the difference between the assumed X and calculated root, if not yet inside tolerance then update root and continue.
# If the calculated root comes inside the tolerance allowed then break out of the loop.
# Print the root.

# my process:
# firstly, the algorithm above is presented in the function to see iof the overall functionality is correct (substitute 1 for x to test)
# then we need to use a loop to iterate for numbers between the guess (input) and 1.
# we need to decide on a tolerance - how close does the calculated root need to be?
# https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
# the above link shows how the process can be envisioned and suggests the following for Newton's algorithm
# x_(n+1) = x_n - f(x_n) / f’(x_n)


# N is the number to find the square root of 
# X changes with each iteration
def sqrt (N,X):
    
    root = 0.5 * (X+(N/X))
    print (root)
    return root

# get a positive float from user

N = float(input ("Please enter a positive number: "))
X = N

# suggest precision to end loop
precision = 10 ** (-10)
while (abs(N-(X*X))>precision):
    
    # apply function to user input
    squareroot_approx = sqrt (N,X)
    print (squareroot_approx)
    X = squareroot_approx
    
    
print (f"The square root of {N} is approximately {squareroot_approx}")

# program is printing each iteration twice??



    

