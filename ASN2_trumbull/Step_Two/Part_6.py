#!/usr/bin/env python3
import numpy as np


def main():
    beforeList = []
    for x in range(0, 10):
        beforeList.append(np.random.randint(0, 11))

    afterList = ["Even" if x % 2 == 0 else "Odd" for x in beforeList]

    print("Before List Comprehension is implemented:")
    print(beforeList)
    print("\nAfter List Comprehension is implemented:")
    print(afterList)


if __name__ == "__main__":
    main()
