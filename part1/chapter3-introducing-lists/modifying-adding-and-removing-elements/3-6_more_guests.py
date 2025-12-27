# You just found a bigger dinner table, so now more space is available.
# Think of three more guests to invite to dinner

# Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program,
# informing people that you found a bigger table


invitees = ['Michael Jackson', 'Bahlil', 'Prabowo']

for i in range (len(invitees)):
    print(f"Hi {invitees[i]}, i found a bigger table for our dinner, therefore, i would like to add three more guests to come over")

invitees.insert(0, 'verrel')
invitees.insert(2, 'ferry irwandi')
invitees.append('Luffy')

for invitee in invitees:
    print(f"Hi {invitee.title()}, i would like to invite you to the special Joshua's Dinner tonight at the White House")

