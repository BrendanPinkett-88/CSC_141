# restaurant

class Restaurant:
    def __init__(self,restaurant_name, food_name):
        self.name = restaurant_name
        self.cuisine_type = food_name

    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

Dreaded_Dinner = Restaurant("Dreaded-Dinner", "American")
Dreaded_Dinner.describe_restaurant()
Dreaded_Dinner.open_restaurant()

def can_toy_take_a_date(self):
    if self.price_range < 50:
       print(f"Don't embarrass yourself. It's too expensive!")
    else:
       print(f"Go ahead and take your date to {self.name}!")