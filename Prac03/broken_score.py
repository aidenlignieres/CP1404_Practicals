"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    user_score = float(input("Enter score: "))
    print(score_result(user_score))


def score_result(result):
    if result < 0 or result > 100:
        return "Invalid score"
    elif result >= 90:
        return "Excellent"
    elif result >= 50:
        return "Passable"
    else:
        return "Bad"


main()
