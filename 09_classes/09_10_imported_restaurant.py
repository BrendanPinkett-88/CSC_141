# imported restaurant.py


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

        
restaurant = Restaurant("Dreaded-Dinner", "American")
restaurant.describe_restaurant()
restaurant.open_restaurant()