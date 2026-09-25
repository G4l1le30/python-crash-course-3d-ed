"""
Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
"""


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


class Privileges:
    """Privilege class"""

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    # display actions that admin can do
    def show_privileges(self):
        for privilege in self.privileges:
            print(f"Admin {privilege}")


class Admin(User):
    """Class to represent admin"""

    def __init__(self, first_name, last_name, age, hobby):
        super().__init__(first_name, last_name, age, hobby)
        self.privileges = Privileges()  # buat object privilege dari class Privileges


user1 = Admin("Joshua", "Hutasoit", 21, "coding")

user1.privileges.show_privileges()  # panggil obcject user1 -> ambil atribut privileges -> panggil fungsi show_privileges
