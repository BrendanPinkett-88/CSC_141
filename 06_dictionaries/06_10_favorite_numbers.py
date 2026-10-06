#cool numbers 2

favorite_numbers = {
    "Peter Parker": [37, 21, 56],
    "Bruce Banner": [12, 95, 43],
    "Steve Rogers": [25, 72, 65],
    "Clint Barton": [42, 89, 29],
    "Tony Stark": [58, 45, 59] 
}

for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are:")
    for number in numbers:
        print(number)