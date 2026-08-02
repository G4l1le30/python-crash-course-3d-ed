"""
Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country
"""


def describe_city(city_name, country="Indonesia"):
    print(f"{city_name.title()} is in {country.title()}")


# 2 country in the default country
describe_city("surabaya")
describe_city("jakarta")

# 1 country not in the default country
describe_city("tokyo", "japan")
