# Question 1
name = input("Input Name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# Question 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Your name is {name}")

# Question 3
in_file = open("numbers.txt", "r")
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
in_file.close()
print(number_1 + number_2)

# Question 4
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)