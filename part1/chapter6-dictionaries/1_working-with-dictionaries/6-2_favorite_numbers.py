"""
Use a dictionary to store people's favorite numbers.
Think of five names, and use them as keys in your directory.
Print each person's name and their favorite number.
For even more fun, poll a few friends and get some actual data for your program
"""

favorite_number = {"joshua": 67, "darvesh": 7, "haris": 9}

for name, number in favorite_number.items():
    print(f"{name.title()}'s favorite number is {number}")
