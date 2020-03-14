"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score > 90 and score <= 100:
    print("Excellent")
elif score > 50 and score < 90:
    print("Passable")
elif score < 50 and score > 0:
    print("Fail")
else:
    print("Not possible")