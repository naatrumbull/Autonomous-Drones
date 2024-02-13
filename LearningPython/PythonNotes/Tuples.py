# tuples are similar to list but  are immutable

numbers = (1, 2, 3, 3, 3)  # use () for tuples
# numbers[0] = 3 *invalid operation. You can't change tuples
print(numbers.count(3))  # returns number of times 3 appears
print(numbers.index(1))  # returns index of first occurence of 1
