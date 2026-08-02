"""
Write different versions of either Exercise 7-4 or 7-5 that do
each of the following at least once:

- Use a conditional test in the while statement to stop the loop.
- Use an active variable to control how long the loop runs.
- Use a break statement to exit the loop when the user enters a 'quit' value.
"""

prompt = "What is your age?\n"
age = ""
validAge = True

# runs when either input is quit or invalid age
while age != "quit" and validAge:
    age = input(prompt)
    if age == "quit":
        break
    if int(age) < 0:
        validAge = False

    elif int(age) < 3:
        print("Your ticket is free")
    elif 3 <= int(age) <= 12:
        print("Your ticket is $10")
    elif int(age) > 12:
        print("Your ticket is $15")
