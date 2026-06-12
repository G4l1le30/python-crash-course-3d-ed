"""
Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.

• Use a loop to print a sentence about each river, such as:
  The Nile runs through Egypt.

• Use a loop to print the name of each river included in the dictionary.

• Use a loop to print the name of each country included in the dictionary.
"""

rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "yangtze": "china",
}

for river in rivers.keys():
    print(f"The {river.capitalize()} runs through {rivers[river].capitalize}")


for river in rivers:
    print(f"{river}")
for country in rivers.values():
    print(f"{country}")
