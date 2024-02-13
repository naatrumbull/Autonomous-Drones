#!/usr/bin/env python3
import numpy as np


def manipulateMatrix(A, B):
    if (A.shape != B.shape):
        raise Exception("Matrices need to be of same size!")

    return np.transpose(A) * B * np.linalg.inv(A)


def main():
    # Testing w/o an exception
    randomMatrix1 = np.random.randint(11, size=(4, 4))
    randomMatrix2 = np.random.randint(11, size=(4, 4))
    print("\nMatrix of Size 4 X 4:\n" + str(randomMatrix1))
    print("\nAnother Matrix of Size 4 X 4:\n" + str(randomMatrix2))
    print("\nCalculating A^(T)*B*A(-1) with the defined function")
    print(manipulateMatrix(randomMatrix1, randomMatrix2))

    # Testing with an exception
    randomMatrix3 = np.random.randint(11, size=(3, 3))
    randomMatrix4 = np.random.randint(7, size=(4, 4))
    try:
        print(manipulateMatrix(randomMatrix3, randomMatrix4))
    except Exception as e:
        print("\nOh no! An exception was found! Here's what is says: " + str(e))
    finally:
        print("Task completed!")


if __name__ == "__main__":
    main()
