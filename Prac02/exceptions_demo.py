"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    # Value erros occure when either the denominator or numerator is a non interagate
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    # A zero division error will occure when the denominator is a zero
    print("Cannot divide by zero!")
print("Finished.")
"""To remove or avoid the possiblity of a ZeroDivisionError it would be ideal to inform/remind the uses that any 
numerator except 0 can be devided by 0 
"""