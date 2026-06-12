"""
Make a list of five or more usernames, including the name 'admin'.
Imagine you are writing code that will print a greeting to each user after they log into a website.
Loop through the list, and print a greeting to each user

If username is admin, print a special greeting, such as 'Hello admin, would you like to see a status report?'
Otherwise, print generit greeting
"""

usernames = ["admin", "joshua", "karma", "shanks", "john", "paul"]

for username in usernames:
    if username == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}")
