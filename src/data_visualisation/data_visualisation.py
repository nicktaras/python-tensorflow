import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

# create a range from 0 - 9
x = np.arange(0, 10) 

# equal to x squared
y = x**2

# plot the data
plt.plot(x, y)

# Pass a string code as a marker
plt.plot(x, y, '*')

# Pass a color code
plt.plot(x, y, 'red')

# Red dashed line
plt.plot(x, y, 'r--')

# The API has a lot of options

# Set x and y limits
plt.xlim(0, 4)
plt.ylim(0, 4)
plt.title("Title Goes Here")
plt.xlabel("X label")
plt.ylabel("X label")

# use show to load the visual 
plt.show()