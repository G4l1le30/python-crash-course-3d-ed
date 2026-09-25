"""
An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote in
Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class
will work; just pick the one you like better. Add an attribute called flavors that
stores a list of ice cream flavors. Write a method that displays these flavors.
Create an instance of IceCreamStand, and call this method
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


class IceCreamStand(Restaurant):
    """A class to represent ice cream stand"""

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(
            restaurant_name, cuisine_type
        )  # ambil atribut dari parent class
        self.flavors = ["chocolate", "vanilla", "strawberry"]

    def get_flavors(self):
        for flavor in self.flavors:
            print(f"we have {flavor}")


ice_cream = IceCreamStand("ice cream josh", "dessert")

ice_cream.get_flavors()
