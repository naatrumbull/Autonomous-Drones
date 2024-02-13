#!/usr/bin/env python3
import numpy as np


def randomReturn():
    randNum = np.random.randint(2)
    return -1 if randNum == 0 else 1


def main():
    for x in range(1, 11):
        print("Trial #{}: ".format(x) + str(randomReturn()))


if __name__ == "__main__":
    main()
