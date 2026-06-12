"""
Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3

Store the numbers 1 through 9 in a list
Loop through the list
Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.
Your output should read '1st 2nd 3rd ...' , and each result should be on a separate line
"""

numbers = [number for number in range(1, 10)]

for number in numbers:
    print(number, end="")
    if number == 1:
        print("st")
    elif number == 2:
        print("nd")
    elif number == 3:
        print("rd")
    else:
        print("th")
