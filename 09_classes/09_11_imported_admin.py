#imported admin.py




print("Privileges class is defined in this file.")  
print("show_privileges() method is defined in this file.")

class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")


class Privileges:
    def __init__(self):
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user"
        ]

    def show_privileges(self):
        print("Administrator privileges:")
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges()



admin = Admin("Brendan", "Pinkett", 18, "Delaware")
admin.privileges.show_privileges()