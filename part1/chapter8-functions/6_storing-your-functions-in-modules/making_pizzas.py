"""Importing an entire module (pizza.py)"""

import pizza

pizza.make_pizza(16, "pepperoni")


"""Importing specific function from the module"""
from pizza import make_pizza

make_pizza(16, "pepperoni", "green peppers")

"""Using 'as' to Give a Function an Alias"""
from pizza import make_pizza as mp

mp(12, "extra cheese")


"""Using 'as' to give module an alias"""
import pizza as p

p.make_pizza(11, "green peppers")

"""Importing All Functions in a Module"""
from pizza import *

make_pizza(10, "extra cheese")
