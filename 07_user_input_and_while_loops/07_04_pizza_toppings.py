#pizza toppings

while True:
    topping = input("Plain Cheese")
    if topping == 'quit':
        pizzas = False
        break
    else:
        print (f"I'll add {topping} to your pizza.")