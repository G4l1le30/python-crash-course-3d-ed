"""
Write a loop that prompts the user to enter a series
of pizza toppings until they enter a 'quit' value.
As they enter each topping, print a message saying you’ll add that topping to their pizza.
"""

prompt = "What toppings would you like for your pizza?\n"
topping = ""
while topping != "quit":
    topping = input(prompt)
    if topping != "quit":
        print(f"Okay! I'll ad {topping} to your pizza")
