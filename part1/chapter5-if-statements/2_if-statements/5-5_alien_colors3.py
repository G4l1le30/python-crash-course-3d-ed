"""
Turn your if else chain from exercise 5-4 into an if-elif-else chain.

If the alien color is green, print a statement that the player just earned 5 points for shooting the alien
If the alien color is yellow, print a statement that the player just earned 10 points
If the alien is red, print a message that the player earned 15 points.

Write three versions of this program, making sure each message is printed
"""

aliens_color = "green"
# aliens_color = 'red'
# aliens_color = 'yellow'
if aliens_color == "green":
    print("You have earned 5 points")
elif aliens_color == "yellow":
    print("You gained 10 points")
else:
    print("You have earned 15 points")
