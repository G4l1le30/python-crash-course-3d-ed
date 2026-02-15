# Start with yourt program from exercise 4-1.
# Make a copy of the list of pizzas, and call it friend_pizzas. Then do the following

# Add a new pizza to the og list
# Add a different pizza to the friend list
# Prove that you have two separate lists.

""" ""
Print the message My favorite piz-
zas are:, and then use a for loop to print the first list. Print the message My
friend’s favorite pizzas are:, and then use a for loop to print the second list.
Make sure each new pizza is stored in the appropriate list
"""

pizzas = ["pizza hut", "dominos pizza", "burger king"]

friend_pizzas = pizzas[:]

pizzas.insert(3, "cheese pizza")
friend_pizzas.append("meat lovers pizza")

print("My favorite pizzas are ", end=" ")
for pizza in pizzas:
    print(pizza, end=", ")

print()
print("My friend's favorite pizzas are ", end=" ")
for pizza in friend_pizzas:
    print(pizza, end=", ")

print()
