import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a)

# Return a specific element [r, c]
print(a[1, 5])  # return 13
print(a[1, -2])  # also return 13

# Get a specific row
print(a[0, :])  # return row 0

# Get a specific columns
print(a[:, 2])  # return column 2

# getting a little more fancy [startindex:endindex:stepsize]
print(a[0, 1:6:2])

# Changing an element
print("\nChanging element [1, 5] to 20")
a[1, 5] = 20
print(a)

# Changing a whole column
print("\nChanging index 2 to '5':")
a[:, 2] = 5  # index 2 in each row will become 5
print(a)

# 3D array
b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3D Array\n" + str(b))

# Getting element from 3D array
print("\nIndex from [0,1,1]\n" + str(b[0, 1, 1]))  # returns 4

# Using : in 3D arrays
print(b[:, 0, :])
