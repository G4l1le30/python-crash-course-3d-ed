"""
An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of
strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method
"""


# User class dari 9-5
class User:
    def __init__(self, first_name, last_name, age, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby
        self.full_name = (first_name + " " + last_name).title()
        self.login_attempts = 0

    def describe_user(self):
        print(
            f"Your name is {self.full_name}, you love to {self.hobby}, and you're {self.age} years old"
        )

    def greet_user(self):
        print(f"Good morning, {self.first_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    """Class to represent admin"""

    def __init__(self, first_name, last_name, age, hobby):
        super().__init__(first_name, last_name, age, hobby)

        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"Admin {privilege}")


user1 = Admin("Joshua", "Hutasoit", 21, "coding")

user1.show_privileges()
