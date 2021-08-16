# example
print("example results")
for i in range(1, 21, 2):
    print(i, end=" ")
print()

# Part A
print("Part A results")
for i in range(0, 100 , 10):
    print(i, end=" ")
print()

# Part B
print("Part B results")
for i in range(20, 0, -1):
    print(i, end=" ")
print()

# Part C
print("Part C results")
star_count = int(input("Number of stars: "))
total_stars = 0
for i in range(star_count+1):
    total_stars = '*'* i
print(total_stars)

# Part D
print("Part D results")
star_count = int(input("Number of stars: "))
total_stars = 0
for i in range(star_count+1):
    print("*"*i)
