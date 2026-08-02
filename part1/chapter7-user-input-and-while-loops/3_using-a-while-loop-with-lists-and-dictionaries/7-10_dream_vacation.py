"""
Write a program that polls users about their dream vaca-
tion. Write a prompt similar to If you could visit one place in the world, where
would you go? Include a block of code that prints the results of the poll.
"""

prompt = "If you could go anywhere in the world, where would it be?\n"

responses = {}

activate = True

while activate:
    name = input("What is your name?\t")
    response = input(prompt)

    responses[name] = response

    loop = input("Is that all? (y/n)\t")
    if loop == "y":
        activate = False

for name, response in responses.items():
    print(f"{name} wants to go to {response}")
