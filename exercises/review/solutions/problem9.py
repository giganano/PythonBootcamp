r"""
The solution to problem 9.
"""

# This solution creates a 5x5 array of random values between 0 and 1 using the
# NumPy random.rand() function. It then creates a colormap using
# plt.cm.get_cmap() with the 'RdBu' argument, which ranges from blue to red.
# Finally, it uses plt.imshow() to create a grid plot of the values, with the
# colormap applied. It also adds a colorbar to the plot to show the mapping
# between values and colors.

# You can customize this code for your specific use case by replacing the
# values variable with your own 2D array of values. You can also customize the
# colormap by choosing a different argument for plt.cm.get_cmap(). For example,
# you can use 'Greens' to create a colormap that ranges from light to dark
# green.

# Now make modifications to this code based on your initials. My name is
# Paarmita Pandey, so I am plotting my initials PP

import numpy as np
import matplotlib.pyplot as plt

# Create a 2D array of random values between 0 and 1
values = np.random.rand(5, 5)

# Create a colormap that ranges from blue to red
cmap = plt.cm.get_cmap('RdBu')

# Create a grid plot using imshow and the colormap
plt.imshow(values, cmap=cmap)

# Add a colorbar to show the mapping between values and colors
plt.colorbar()

# Show the plot
plt.show()

# Create a 10x10 grid of Random numbers between 0 and 1
grid = np.random.rand(10, 10)

# Set the pixels for the letter "P" (first occurrence) (you can use any
# positive or negative value higher than 1, so that the initials are of
# different color than rest of the grid)
grid[0:5, 0] = -1.5
grid[0, 1:3] = -1.5
grid[2, 1:3] = -1.5
grid[1,2] = -1.5
# Set the pixels for the letter "P" (second occurrence)
grid[0:5, 4] = -1.5
grid[0, 5:7] = -1.5
grid[2, 5:7] = -1.5
grid[1,6] = -1.5
cmap = plt.cm.get_cmap('RdYlGn')

# Create a grid plot using imshow and the colormap
plt.imshow(grid, cmap=cmap)

# Add a colorbar to show the mapping between values and colors
plt.colorbar()

# Show the plot
plt.show()



