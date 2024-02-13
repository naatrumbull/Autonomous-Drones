#!/usr/bin/env python3
import numpy as np


def main():
    beforeList = []
    for x in range(0, 10):
        beforeList.append(np.random.randint(0, 11))

    print("Before List Comprehension is implemented:")
    print(beforeList)

    afterList = [x if x < 5 or x > 7 else 0 for x in beforeList]
    print("\nAfter List Comprehenstion is implemented:")
    print(afterList)


if __name__ == "__main__":
    main()
