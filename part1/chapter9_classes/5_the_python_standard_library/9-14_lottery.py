"""
Make a list or tuple containing a series of 10 numbers and 5 letters.
Randomly select 4 numbers or letters from the list and print a message saying that
any ticket matching these 4 numbers or letters wins a prize.
"""

from random import choice


def lottery():
    seq = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "A", "Z", "D", "G", "P")
    winning_ticket = []
    for i in range(4):
        char = choice(seq)
        winning_ticket.append(str(char))

    print("".join(winning_ticket))
