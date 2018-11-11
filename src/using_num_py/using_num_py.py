import numpy as np

# Create array
my_list = [1, 2, 3]

# us numpy to create an n dimensional array
type(np.array(my_list))

# Create an array within numpy
arr = np.array(my_list)

# Create a range 0 to 9 (start and stop, optional jump/step size as third params)
np.arange(0, 10)

# Creates a one dimensional array of 0's
# e.g. [0, 0, 0, 0, 0]
np.zeros(5)

# Creates a two dimensional array of 0's
# e.g. 
# [0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0]
np.zeros(3, 5)

# Create ones instead
# [0, 0, 0]
np.ones(3)

# Similar to arrange (the third params asks how many decimal places 
# would you like between each step)
# (start, stop, points between)
np.linespace(0, 11, 11)

# Random int generator
np.randint(0,10)

# 2 dimensional random int
np.randint(0,1000, (3, 3))

# seed allows us to keep getting the same set of random numbers
# useful for testing
np.random.seed(101)
np.random.seed(0, 1000, 10)

# get max or min of an array
np.random.seed(101)
arr = np.random.seed(0, 1000, 10)
arr.min()
arr.max()
arr.mean()

# Reshape the array
arr.reshape(2, 5)

# to get values from a dimensional array
# assign mat to the array mat = array...
mat[0, 1]

# slice a row
# : means everything
mat[:, 0]

# slice a row
mat[5, :]

# slices (grab first three in 2 array)
mat[0:3, 0:3]

# is this matrix greater than 50 for each value
# turns the array into bools
my_filer = mat > 50

# returns values greater than 50
mat[mat > 50]










