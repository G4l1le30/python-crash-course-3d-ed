"""
Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary,
and store one to three favorite places for each person.
To make this exercise a bit more interesting, ask some friends to name a few of their favorite places.
Loop through the dictionary, and print each person’s name and their favorite places.
"""

favorite_places = {
    "Joshua": ["beach", "cafe", "germany"],
    "Felix": ["japan", "US", "library"],
    "Chuck": ["home", "yard", "pool"],
}
for name, place in favorite_places.items():
    print(f"{name}'s favorite places are {', '.join(place)}")
