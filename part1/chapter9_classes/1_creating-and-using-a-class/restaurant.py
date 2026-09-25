"""
9-1.
Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indi-
cating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attri-
butes individually, and then call both methods.
"""


class Restaurant:
    """A class to model a Restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name} where we serve {self.cuisine_type}")

    def open_restaurant(self):
        print("Restaurant is now open!")


restaurant = Restaurant("Top Eats", "Indonesian cuisine")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.open_restaurant()
restaurant.describe_restaurant()
