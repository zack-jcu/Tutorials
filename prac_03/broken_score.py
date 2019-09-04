"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    classification_result = score_classification(score)
    print(classification_result)


def score_classification(score):
    if score > 90 and score < 100:
        classification_result = "Excellent"
    elif score >= 50 and score < 90:
        classification_result = "Passable"
    elif score > 0 and score < 50:
        classification_result = "Bad"
    return (classification_result)


main()
