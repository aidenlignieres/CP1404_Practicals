numbers = [3, 1, 4, 1, 5, 9, 2]

"""Answers for following expressions:
numbers[0] answer would be 3
numbers[-1] answer would be 2
numbers[3] answer would be 1
numbers[:-1] answer would be 3, 1, 4, 1, 5, 9
5 in numbers would be true/ position 4
7 in numbers would be false/ error, invalid
"3" in numbers would be false/ error, non integer
numbers + [6, 5, 3] should be added onto the list
"""
print("initial stating list \n{}\n".format(numbers))

"""Task 1 in warm up"""
numbers[0] = "ten"
print("changed first element in list to str(ten) \n{}\n".format(numbers))

"""Task 2 in warmup"""
numbers[-1] = 1
print("changed last element in list to int(1) \n{}\n".format(numbers))

"""Task 3 in warmup"""
print("Get element from numbers except the first 2")
for element in range(2, len(numbers)):
    print(element)

"""Task 4 in warmup"""
print("\nCheck if 9 is an element of numbers")
if len(numbers) == 9:
    print("The numbers list has 10 elements")
else:
    print("The numbers list has less than 10 elements")
