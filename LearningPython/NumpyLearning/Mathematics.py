import numpy as np

a = np.array([1, 2, 3, 4])
print(a)

# Some basic math with matrix
print("\nExample #1")
print(a + 2)  # a + 2 returns a with each int increased by 2. Note that a is not changed
print(a - 2)
print(a/2)
print(a*2)

array1 = np.array([1, 2, 3, 4])
array2 = np.array([2, 2, 2, 2])

print("\nExample #2")
print(array1 * array2)
print(array1 ** array2)  # array1^(array2)
print(array2 ** array1)
print(array1 ** -1.0)
print(array2 / array1)
print(array1 // array2)
print(np.sin(array2))  # takes the sine of matrix
