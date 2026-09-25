from user import User


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
