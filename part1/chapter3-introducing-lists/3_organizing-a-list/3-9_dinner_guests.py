"""
working with one of the programs from exercises 3-4 through 3-7, use len() to print a message indicating the number 
of people you're inviting to dinner
"""

#code from exercise 3-7 


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


print(f"{len(invitees)} people are invited to the dinner")