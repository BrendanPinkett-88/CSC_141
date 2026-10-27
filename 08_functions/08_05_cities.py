#cities
def describe_city(city, country="USA"):
    print(f"{city.title()} is in {country.title()}.")

describe_city("Reykjavik")
describe_city("Akureyri")
describe_city("Paris", "France")