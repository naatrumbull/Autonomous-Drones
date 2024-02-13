import numpy as np

# fill matrix with 0. The parameter take a tuple!!
print("One Dimensional")
print(np.zeros((5)))
print(np.zeros((2, 3)))
print(np.zeros((3, 4, 3)))

# fill matrix with 1
print(np.ones((4, 2, 2)))

# fill matix with any other number
print(np.full((2, 3), 4))  # fills a 2X4 array with 4

# Random decimal numberr. Parameter takes (rows, cols) and not tuples
print(np.random.rand(4, 2))

# Random integer values
# makes 3X3 array with random ints from 0 to 1
print(np.random.randint(2, size=(3, 3)))
