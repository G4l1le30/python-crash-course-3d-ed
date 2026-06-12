"""
Make several dictionaries, where each dictionary represents a different pet.
In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets.
Next, loop through your list and as you do, print everything you know about each pet.
"""

pet = {"animal": "bird", "owner": "Joshua"}

pet1 = {"animal": "reptiles", "owner": "john"}
pet2 = {
    "animal": "mammal",
    "owner": "Deo",
}
pets = [pet, pet1, pet2]
for p in pets:
    print(f"{p['owner']} has a {p['animal']} as his pet")
