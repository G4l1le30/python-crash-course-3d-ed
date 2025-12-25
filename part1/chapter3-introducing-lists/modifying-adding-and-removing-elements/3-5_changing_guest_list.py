# You heard that one of your guests can’t make the dinner, 
# so you need to send out a new set of invitations. 
# You’ll have to think of someone else to invite 


# Start with your program from Exercise 3-4. Add a print() call at the end of your program, 
# stating the name of the guest who can’t make it 

invitees = ['michael Jackson', 'Nicola Tesla', 'prabowo']


for invitee in invitees:
    print(f"Hi {invitee.title()}, i would like to invite you to the special Joshua's Dinner tonight at the White House")
    
absentInvitee = invitees.pop(1)
print(f"{absentInvitee.title()} can't make it due to personal issue.")

# Modify your list, 
# replacing the name of the guest who can’t make it with the name of the new person you are inviting. 

invitees.insert(1, 'bahlil') 

# Print a second set of invitation messages, one for each person who is still in your list. 


for invitee in invitees:
    print(f"Hi {invitee.title()}, i would like to invite you to the special Joshua's Dinner tonight at the White House")
    