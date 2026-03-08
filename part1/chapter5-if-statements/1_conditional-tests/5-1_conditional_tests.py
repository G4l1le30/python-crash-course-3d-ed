"""
write a series of conditional tests. Print a statement describing each test and your prediction for ther results of each test.
Your code should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.

"""

import random

univ = ["brawijaya", "indonesia", "cendrawasih", "padjajaran"]
isTrue = random.choice(univ)
prediction = random.choice(univ)


print(f"Is univ == {prediction}? I predict True")
print(isTrue == prediction)
print(f"It is {isTrue}")
