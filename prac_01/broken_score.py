"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
"""
score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
else:
    if score > 100:
        print("Invalid score")
    if score > 50:
        print("Passable")
    if score > 90:
    print("Excellent")
if score < 50:
    print("Bad")
"""

score = float(input("Enter score: "))
if score > 90 and score < 100:
    print("Excellent")
elif score >= 50 and score < 90:
    print("Passable")
elif score > 0 and score < 50:
    print("Bad")
else:
    print("Invalid number")