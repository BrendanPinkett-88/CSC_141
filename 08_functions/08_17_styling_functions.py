# styling functions
def style_function():
    print("This is a styled function.")

    def city_country(city, country):
    """Return a city and its country."""
    return f"{"city"}, {"country"}"


print("city_country"("Santiago", "Chile"))
print("city_country"("Paris", "France"))
print("city_country"("Tokyo", "Japan"))

def describe_city(city, country="Iceland"):
    """Print a sentence describing a city."""
    print(f"{city} is in {country}.")


describe_city("Reykjavik")
describe_city("Akureyri")
describe_city("Paris", "France")

def show_messages(messages):
    """Print each message in a list."""
    for message in messages:
        print(message)


text_messages = [
    "Hello, how are you?",
    "Have a great day!",
    "See you later!",
]

show_messages(text_messages)