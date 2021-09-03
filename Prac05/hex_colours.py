"""
Search for colour hex decimals
by using color name
"""

CODE_TO_NAME = {
    "rosybrown": "	#bc8f8f",
    "saddlebrown": "#8b4513",
    "sandybrown": "#f4a460",
    "slategray": "#708090",
    "yellowgreen": "#9acd32",
    "whitesmoke": "#f5f5f5",
    "violetred": "#d02090",
    "navyblue": "#000080",
    "plum": "#dda0dd",
    "tan": "#d2b48c"
                }

print("Please enter the colour name to find hex for colour.")
colour_name = input("Colour name: ").lower()


while colour_name != "":
    # pass
    if colour_name in CODE_TO_NAME:
        print("The hex code for {} is {}".format(colour_name, CODE_TO_NAME[colour_name]))
    else:
        print("That colour is not in dictionaries.")
        print("Please enter a valid colour")
    colour_name = input("Colour name: ")
