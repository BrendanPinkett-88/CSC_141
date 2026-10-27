#city names
def city_name(city, country):
    return f"{city.title()}, {country.title()}"

print(city_name("Santiago", "Chile"))
print(city_name("London", "England"))
print(city_name("Tokyo", "Japan"))