#think of at least 5 places in the world you'd like to visit

"""
- store the locations in a list. Make sure the list is not in alphabetical order.
- print your list in its original raw order
- use sorted() function to print your list in alphabetical order without modifying the actual list
- show that your list is still in its original order by printing it
- use sorted() to print your list in reverse-alphabetical order without changing the actual list
- show that your list is still in its original order by printing it again
- use reverse() method to change the order of your list. Print the lsit to show that its order has changed
- use reverse() to change the order of your list again. Print the lsit to show that its back to its original order
- use sort() method to change your list so its stored in alphabetical order. Print the lsit to show that its order has changed
- use sort() to change your list so its stored in reverse-alphabetical order. Print the lsit to show that its order has changed

"""

locations = ['france', 'japan','australia','italy','swiss']
print(f"original list: {locations}")

#implement sorted() function
print(f"using sorted() function: {sorted(locations)}")
print(f"original list has not changed: {locations}")

print()

# sorted function in reverse-alphabetical
print(f"sorted reverse-alphabetical: {sorted(locations, reverse=True)}")
print(f"original list: {locations}")

print()

# use reverse method
locations.reverse()
print(f"list has been reversed permanently: {locations}")
locations.reverse()
print(f"back to original lsit: {locations}")
print()
#sort in alphabetical order
locations.sort()
print(f"sort in alphabetical order permanently: {locations}")

#sort in reverse-alphabetical order
locations.sort(reverse=True)
print(f"sort in reverse alpphabetical order: {locations}")
