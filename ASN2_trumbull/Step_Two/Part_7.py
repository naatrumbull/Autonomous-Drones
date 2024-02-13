#!/usr/bin/env python3
import numpy as np


def main():
    I = np.random.randint(256, size=(256, 256))
    Is = np.zeros((3, 256, 256))

    for x in range(0, 3):
        Is[x, :, :] = I

    print("Array I:")
    print(I)
    print("\nArray Is:")
    print(Is)


if __name__ == "__main__":
    main()
