from base64 import b16decode
import numpy as np

# creating an array
a = np.array([1, 2, 3], dtype="int16")
print(a)

# Creating non-ragged 2D array
b = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
print(b)

# return number of dimenstions of an array
print(a.ndim)  # 1 dimensions in a
print(b.ndim)  # 2 dimensions in b

# For vectors! Will print in form (rows, cols)
print(a.shape)  # Prints (3,)
print(b.shape)  # Prints (2, 4)

# Get Type
print(a.dtype)  # prints int16
print(b.dtype)  # prints int32

# returns number of bytes that a single item takes in memory!
print(a.itemsize)  # Array a takes 2 bytes for each int

# size returns number of elements in an array
print(b.size)  # 8 total elements
print(a.size)  # 3 total elements

# return total size in bytes that an array uses!
print(a.nbytes)  # 3 ints * 2 bytes each = 6
print(b.nbytes)  # 8 ints * 4 bytes each = 32
