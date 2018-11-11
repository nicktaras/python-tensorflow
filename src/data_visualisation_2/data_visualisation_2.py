import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

# pandas also has a visual lib (built on matplotlib)
# e.g. df.plot(x='salary', kind='scatter')

# Create a matrix
mat = np.random.randint(0, 1000, (10, 10))
# Use imshow to display the values in relation to color
plt.imshow(mat)
# adds color bar to show the range
plt.colorbar()
# use show to load the visual 
plt.show()