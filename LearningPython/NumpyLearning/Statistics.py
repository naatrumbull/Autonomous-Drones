import numpy as np

stats = np.array([[1, 2, 3], [4, 5, 6]])
print(stats)
print(np.min(stats))
print(np.max(stats))
print(np.max(stats, axis=0))
print(np.sum(stats, axis=1))

# The axis = 0 refers to going down the columns from left to right.
# The axis = 1 refers to going through each row, from top to bottom
