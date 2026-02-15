"""
A buffet-style restaurant offers only five basic foods.
Think of five simple foods, and store them in a tuple

- Use a for loop to print each food the restaurant offers
- Try to modify on of the items, and make sure that python reject the change
- The restaurant changes its menu, replacing two of the items with different foods.
  Add a line that rewrites the tuple, and then use a for loop to print
  each of the items on the revised menu.
"""

basic_foods = ("ayam pop", "rendang", "ikan nila", "gurame", "ayam laos")

for basic_food in basic_foods:
    print(basic_food)

try:
    basic_foods[0] = "you got hacked!"
except TypeError as e:
    print(f"Terjadi error karena {e}")


for basic_food in basic_foods:
    print(basic_food)

# changin restaurants menu

basic_foods = ("es jeruk", "es mangga", "jus jambu", "jus sirsak", "soda gembira")
print("Restoran berhasil mengubah menu")
for basic_food in basic_foods:
    print(basic_food)
