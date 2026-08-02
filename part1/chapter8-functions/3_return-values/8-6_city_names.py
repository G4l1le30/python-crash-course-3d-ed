"""
Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the values
that are returned.
"""


def city_country(city_name, country_name):
    return f"{city_name}, {country_name}".title()


city1 = city_country("jakarta", "indonesia")

city2 = city_country("malang", "indonesia")

city3 = city_country("paris", "france")

print(city1)
print(city2)
print(city3)
