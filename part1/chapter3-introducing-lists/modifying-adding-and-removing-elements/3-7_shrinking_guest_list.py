# You just found out that your new dinner table won't arrive in time for the dinner,
# and now you have space for only two guests

# Start with your program from exercise 3-6. 
# Add a new line that prints Add a new line that prints a message saying that you can invite only
# two people for dinner.

# Use pop() to remove guests from your list one at a time until only two names remain in your list. 
# Each time you pop a name from your list, 
# print a message to that person letting them know you’re sorry you can’t invite them to dinner

# Print a message to each of the two people still on your list, letting them know they’re still invited

# Use del to remove the last two names from your list, so you have an empty list
invitees = [
    'verrel', 'Michael Jackson',
    'ferry irwandi', 'Bahlil', 
    'Prabowo', 'Luffy'
    ]


print("I'm sorry for the inconvinience, but i found out that my new table won't arrive in time for dinner")


while len(invitees)>2:
    canceledGuest = invitees.pop()
    print(f"Sorry {canceledGuest.title()}, i can't invite you to dinner")

for invitee in invitees:
    print(f"Mr/Ms {invitee} still invited")

for i in range(len(invitees)):
    del invitees[0]

print(invitees)