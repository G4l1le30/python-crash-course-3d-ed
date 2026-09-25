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
