"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    user_score = float(input("Enter score: "))
    print(score_result(user_score), end="\n\n")

    print("Computer generated score from a range of -10 to 110")
    computer_score = random.randint(-10, 110)
    print(f"generated score is: {computer_score}")
    print(score_result(computer_score))


"""
def random_score_test():
    print("Computer generated score from a range of -10 to 110")
    computer_score = random.randint(-10, 110)
    print(f"generated score is: {computer_score}")
    print(score_result(computer_score))
"""


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
# random_score_test()
