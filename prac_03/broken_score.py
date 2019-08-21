"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    result = score_classification(score)
    print(result)


def score_classification(score):
    if score > 90 and score < 100:
        result = "Excellent"
    elif score >= 50 and score < 90:
        result = "Passable"
    elif score > 0 and score < 50:
        result = "Bad"
    return (result)


main()
