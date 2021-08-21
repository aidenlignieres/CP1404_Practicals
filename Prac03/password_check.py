"""
Password Checker
must set a minimum length
can require some/non special cases
must display password as an *
"""

MIN_LENGTH = 10

print("Please enter a valid password.")
print("Password must contain atleast", MIN_LENGTH, "characters.")

password = input(">")
while len(password) < MIN_LENGTH:
    print("Invalid password")
    print("Please enter a valid password")

    password = input(">")

print("Password is valid")
print("Password:", len(password) * '*')