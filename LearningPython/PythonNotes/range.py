
print("Experiment #3")

numbers = range(5)  # range of number from 0 to 4
print(numbers)

for number in numbers:
    print(number)

print("Experiment #2")

for i in range(24, 29):  # prints from 24 to 28
    print(i)

print("Experiment #3:")

for i in range(0, 11, 2):  # prints from 0 to 10, skipping every other
    print(i)

names = ["Mario", "Zelda", "Irvin"]
for i in names:
    print(str(names.index(i)) + 1 + ": " + i)
