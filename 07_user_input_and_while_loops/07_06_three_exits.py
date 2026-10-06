#three exits

# Exit 1: Using a flag
active = True
topping = "pepperoni"

while topping != "quit":
    topping = input("Enter a pizza topping (or 'quit' to stop): ")

    if topping != "quit":
        print(f"I'll add {topping} to your pizza.")

# Exit 2: Using break
active = True

while active:
    topping = input("Enter a pizza topping (or 'quit' to stop): ")

    if topping == "quit":
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")

# Exit 3: Using continue
while True:
    topping = input("Enter a pizza topping (or 'quit' to stop): ")

    if topping == "quit":
        break

    print(f"I'll add {topping} to your pizza.")