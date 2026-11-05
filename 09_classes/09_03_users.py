# users

class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = "Brendan"
        self.last_name = "Pinkett"
        self.email = "brendan.pinkett001@example.com"

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}, Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

    login_attempts = 0    