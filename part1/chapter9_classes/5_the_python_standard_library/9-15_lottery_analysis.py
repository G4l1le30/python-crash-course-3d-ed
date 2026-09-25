"""
You can use a loop to see how hard it might be to win
the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write
a loop that keeps pulling numbers until your ticket wins. Print a message report-
ing how many times the loop had to run to give you a winning ticket.
"""

from lottery import lottery

my_tickets = ["54A0", "132D", "393P", "605D", "72G0", "D8P7"]

winning_ticket = lottery()
if winning_ticket in my_tickets:
    print("You Win")
else:
    print(f"You Lose\nYour ticket: {my_tickets}\nWinning ticket: {winning_ticket}")
