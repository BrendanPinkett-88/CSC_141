# extending

cities = {
    "New York": {
        "country": "United States",
        "population": 8400000,
        "fact": "New York City is home to the Statue of Liberty.",
        "language": "English",
        "famous_for": "Times Square",
        "nickname": "The Big Apple"
    },
    "Paris": {
        "country": "France",
        "population": 2100000,
        "fact": "Paris is known as the City of Light.",
        "language": "French",
        "famous_for": "The Eiffel Tower",
        "nickname": "The City of Light"
    },
    "Tokyo": {
        "country": "Japan",
        "population": 14000000,
        "fact": "Tokyo is one of the largest cities in the world.",
        "language": "Japanese",
        "famous_for": "Tokyo Tower",
        "nickname": "The Eastern Capital"
    }
}

for city, information in cities.items():
    print(f"\n--- {city} ---")
    print(f"Country: {information['country']}")
    print(f"Population: {information['population']:,}")
    print(f"Language: {information['language']}")
    print(f"Famous for: {information['famous_for']}")
    print(f"Nickname: {information['nickname']}")
    print(f"Fact: {information['fact']}")