"""
Start with the program you wrote for Exercise 6-1 (page 98).
Make two new dictionaries representing different people, and store all three dictionaries in a list called people.
Loop through your list of people. As you loop through the list, print everything you know about each person.
"""

person = {
    "first_name": "Joshua",
    "last_name": "hutasoit",
    "age": 21,
    "city": "Jawa Timur",
}
person1 = {
    "first_name": "Kesya",
    "last_name": "Stevany",
    "age": 20,
    "city": "Jakarta Timur",
}
person2 = {
    "first_name": "Karina",
    "last_name": "Karman",
    "age": 19,
    "city": "Jakarta Timur",
}


people = [person, person1, person2]

for person in people:
    print(
        f"{person['first_name'].title() + ' ' + person['last_name'].title()} is {person['age']} years old and lives in {person['city']}"
    )
