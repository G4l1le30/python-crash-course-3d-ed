"""
Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
Create a dictionary of information about each city and include the country that the city is in, its approximate population,
and one fact about that city.
The keys for each city’s dictionary should be something like country, population, and fact.
Print the name of each city and all of the information you have stored about it.
"""

cities = {
    "Jakarta": {
        "country": "Indonesia",
        "approximate_population": "42 Million",
        "fact": "a capital city of Indonesia",
    },
    "Malang": {
        "country": "Indonesia",
        "approximate_population": "965 Thousands",
        "fact": "known as the Switzerland of Java",
    },
    "Surabaya": {
        "country": "Indonesia",
        "approximate_population": "3 Million",
        "fact": "The second biggest city in Indonesia",
    },
}

for city, information in cities.items():
    print(f"""{city} is a city in {information["country"]} with approximate population of {information["approximate_population"]} people.
A fun fact of {city} is its {information["fact"]}
          """)
