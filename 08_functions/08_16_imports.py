# imports
def city_country(city, country):
    return f"{city}, {country}"

import city_functions

print(city_functions.city_country("Santiago", "Chile"))


from city_functions import city_country

print(city_country("Paris", "France"))


from city_functions import city_country as cc

print(cc("Tokyo", "Japan"))