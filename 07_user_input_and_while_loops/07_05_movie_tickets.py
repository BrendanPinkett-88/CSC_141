#movie tickets

while True:
    age = input("How old are you? (Enter 'quit' to exit) ")
    
    if age == 'quit':
        break
    
    age = int(age)
    
    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")