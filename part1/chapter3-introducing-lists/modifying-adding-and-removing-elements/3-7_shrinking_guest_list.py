# You just found out that your new dinner table won't arrive in time for the dinner,
# and now you have space for only two guests

# Start with your program from exercise 3-6. 
# Add a new line that prints 

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