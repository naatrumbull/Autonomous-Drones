names = ["John", "Bob", "Mosh", "Sam", "Mary"]
print(names[0])  # represent first element in list
print(names[-1])  # represent last element in the list
# print(names[-6]) this will not be found
print(names[0:3])  # O is inclusive, 3 is not inclusive

numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers.append(6)
print(numbers)
numbers.insert(0, 9)
print(numbers)
print(4 in numbers)  # true if 4 is found in list
print("Num elements in list: " + str(len(numbers)))
numbers.remove(9)  # this function removes the number 9 and not index 9
print(numbers)
numbers.clear()
print(numbers)
