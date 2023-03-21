# display a histogram of a normal distribution of 1000 values with a mean of 5 and standard deviation of 2;
# display a plot of the function h(x)=x cubed in the range [0-10]
# author: john kelleher

# https://www.w3schools.com/python/numpy/numpy_random_normal.asp
# distplot is deprecated in next Seaborn version
# https://cmdlinetips.com/2020/09/seaborn-version-0-11-0-is-here-with-displot-histplot-and-ecdfplot/#:~:text=displot()%20is%20the%20new,most%20of%20the%20plotting%20capabilities.


import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns

# create a dataset with the above parameters
x = np.random.normal(loc=5, scale=2, size=(1000))


# display the histogram
plt.hist(x)

# create function
# https://www.tutorialspoint.com/how-to-plot-a-function-defined-with-def-in-python-matplotlib

'''
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True





def f(x):
    # https://numpy.org/doc/stable/reference/generated/numpy.power.html
    x1 = np.arange(10)
    y = np.power(x1,3)
    return y

cubed = f(x)
print (cubed)

x = np.linspace(-10, 10, 100)

plt.plot(x, cubed, color='red')

plt.show()
'''
# the commented out code above is from the previous link
# I have adapted this code to incorporate the requested function

# https://matplotlib.org/stable/tutorials/introductory/customizing.html
'''
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
'''

# define the cubed function
def cubed(x):
   return np.power(x,3)

# set range 0-10
x = np.arange(11)

plt.plot(x, cubed(x), color='red')

plt.show()

