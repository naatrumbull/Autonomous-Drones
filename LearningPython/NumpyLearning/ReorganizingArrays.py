import numpy as np

before = np.array([1, 2, 3, 4], [5, 6, 7, 8])
print(before)

after = before.reshape((2, 2, 2))
print(after)
print(before)
