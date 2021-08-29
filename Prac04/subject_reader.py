"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and displays"""
    # data = get_data()
    # print(data)
    display_subject_details(get_data())


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_details = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        subject_details.append(parts)
        # print(subject_details)
        # print("----------")
    input_file.close()
    # print(subject_details)
    return subject_details


def display_subject_details(subject_details):
    """displays data neatly"""
    for list in subject_details:
        # print(list)
        print("{} is taught by {:12} and has {:3} students".format(*list))
    # pass


main()
