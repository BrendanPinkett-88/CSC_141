# 3 dictonaries

person1 = {
    "first_name": "Robert",
    "last_name": "Downey Jr",
    "age": 61,
    "city": "New York City"
}

person2 = {
    "first_name": "Chris",
    "last_name": "Evans",
    "age": 45,
    "city": "Boston, Massachusetts"
}

person3 = {
    "first_name": "Mark",
    "last_name": "Ruffalo",
    "age": 58,
    "city": "Keosha, Wisconsin"
}

people = [person1, person2, person3]

for person in people:
    print("\nPerson:")
    print(f"First name: {person['first_name']}")
    print(f"Last name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")