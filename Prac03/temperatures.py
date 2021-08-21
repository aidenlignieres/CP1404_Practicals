"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():
    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"
    print(MENU)

    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            value = float(input("Celsius: "))
            print("Result: {:.2f} F".format(conversions("fahrenheit", value)))
        elif choice == "F":
            value = float(input("Fahrenheit: "))
            print("Result: {:.2f} F".format(conversions("celsius", value)))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def conversions(temp_style, value):
    if temp_style == "celsius":
        converted_temp = 5 / 9 * (value - 32)
    elif temp_style == "fahrenheit":
        converted_temp = value * 9.0 / 5 + 32
    return converted_temp


main()
