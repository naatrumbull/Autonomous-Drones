#! /usr/bin/env python3

import numpy as np

print("Matrix A")
A = np.random.rand(3, 3)
print(A)

print("\nMatrix B")
B = np.random.rand(3, 3)
print(B)

# Part a
print("\nPart a")
print("A*B")
print(A*B)

# Part b
print("\nPart b")
print("A o B")
print(A*B)

# Part c
print("\nPart c")
print("A^T*B*A^(-1)")
print(np.transpose(A) * B * np.linalg.inv(A))

# Part d
print("\nPart d")
Av = np.reshape(A, (9, 1))
Bv = np.reshape(B, (9, 1))
print("Av")
print(Av)
print("\nBv")
print(Bv)

print("\nConcatinating Av and Bv into Cv")
Cv = np.concatenate((Av, Bv), axis=1)
print("Cv")
print(Cv)

# Part e
print("\nL2 norm of Cv")
print(np.linalg.norm(Cv, axis=1))
