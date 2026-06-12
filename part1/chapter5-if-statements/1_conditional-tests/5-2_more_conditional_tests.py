"""
If you want to try more comparisons, write more tests and add them
to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list

"""

import random

univ = ["brawijaya", "indonesia", "cendrawasih", "padjajaran"]

for i in range(0, 6):
    isTrue = random.choice(univ)
    prediction = random.choice(univ)

    print(f"Is univ == {prediction}? I predict True")
    print(isTrue == prediction)
    print(f"It is {isTrue}")

for i in range(6, 11):
    isTrue = random.choice(univ)
    prediction = random.choice(univ)

    print(f"is univ != {prediction}? I predict True")
    print(isTrue != prediction)
    print(f"it is {isTrue}")
