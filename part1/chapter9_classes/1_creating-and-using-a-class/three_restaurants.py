"""
9-2
Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
"""

from restaurant import Restaurant

restaurant1 = Restaurant("Sakura House", "Japanese")
restaurant2 = Restaurant("La Tavola", "Italian")
restaurant3 = Restaurant("Seoul Garden", "Korean")

print(restaurant1.describe_restaurant())
print(restaurant2.describe_restaurant())
print(restaurant3.describe_restaurant())
