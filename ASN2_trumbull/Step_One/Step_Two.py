#!/usr/bin/env python3
import numpy as np

I = np.random.randint(256, size=(256, 256))

print("Our image before changes:")
print(I)

M = np.random.randint(2, size=(256, 256))

# Iterates through mask M and changes all corresponding image I values to 0
for row in range(0, 256):
    for col in range(0, 256):
        if M[row][col] == 1:
            I[row][col] = 0

print("\nMask array:\n" + str(M))
print("\nimageArray after applying the mask:\n" + str(I))
