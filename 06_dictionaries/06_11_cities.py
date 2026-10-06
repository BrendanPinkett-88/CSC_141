# cool cities

cities = {
    "New York": {
        "country": "United States",
        "population": 8400000,
        "fact": "New York City is home to the Statue of Liberty."
    },
    "Paris": {
        "country": "France",
        "population": 2100000,
        "fact": "Paris is known as the City of Light."
    },
    "Tokyo": {
        "country": "Japan",
        "population": 14000000,
        "fact": "Tokyo is one of the largest cities in the world."
    }
}

for city, information in cities.items():
    print(f"\nCity: {city}")
    print(f"Country: {information['country']}")
    print(f"Population: {information['population']}")
    print(f"Fact: {information['fact']}")