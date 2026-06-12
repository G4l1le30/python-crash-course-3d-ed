"""
Modify your program from Exercise 6-2 (page 98) so each person can have more than one favorite number.
Then print each person’s name along with their favorite numbers.
"""

favorite_number = {
    "joshua": [67, 90, 100],
    "darvesh": [7, 71, 12],
    "haris": [9, 17, 3],
}

for name, numbers in favorite_number.items():
    print(f"{name.title()}'s favorite number are: ")
    for number in numbers:
        print(f"\t{number}")
