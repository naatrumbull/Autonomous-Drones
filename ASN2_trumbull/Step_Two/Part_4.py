#!/usr/bin/env python3
import numpy as np


def main():
    # Part A
    print("\nPart A")
    listA = ["F", "A", "M", "I", "L", "Y"]
    tupleA = tuple(listA)
    print("listA type: " + str(type(listA)))
    print("tupleA type: " + str(type(tupleA)))

    # Part B
    print("\nPart B")
    listB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arrayB = np.array(listB)
    print("listB type: " + str(type(listB)))
    print("arrayB type: " + str(type(arrayB)))

    # Part C
    print("\nPart C")
    listC = ["H", "L", "L", "E", "O", "P", "H", "H"]
    listCPositions = [1, 3, 4, 2, 5, 2, 2, 2]
    dictionaryC = dict(zip(listC, listCPositions))
    print("listC: " + str(listC))
    print("listC type: " + str(type(listC)))
    print("dictionaryC: " + str(dictionaryC))
    print("dictionaryC type: " + str(type(dictionaryC)))


if __name__ == "__main__":
    main()
