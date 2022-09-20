#!/usr/bin/python3
for numbers_1 in range(0, 9):
    for numbers_2 in range(1, 10):
        if numbers_1 < numbers_2:
            if numbers_1 == 8:
                print("{}{}".format(numbers_1, numbers_2), end="")
            else:
                print("{}{},".format(numbers_1, numbers_2), end=" ")
print()
