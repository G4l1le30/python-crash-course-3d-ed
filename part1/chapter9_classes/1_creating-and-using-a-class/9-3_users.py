"""
Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both meth-
ods for each user.
"""


class User:
    def __init__(self, first_name, last_name, age, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby
        self.full_name = (first_name + " " + last_name).title()

    def describe_user(self):
        print(
            f"Your name is {self.full_name}, you love to {self.hobby}, and you're {self.age} years old"
        )

    def greet_user(self):
        print(f"Good morning, {self.first_name}")


user1 = User("Joshua", "Hutasoit", 21, "Play piano")
user2 = User("Bryan", "Panggabean", 21, "Play guitar")
user3 = User("Agradi", "Juandarma", 21, "Play guitar")

user1.greet_user()
user1.describe_user()

user2.greet_user()
user2.describe_user()

user3.greet_user()
user3.describe_user()
