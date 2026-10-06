# cool places

favorite_places = {
    "Richard": ["New York", "Paris",],
    "Jerimiah": ["Miami", "London"],
    "Rashod": ["Los Angeles", "Hawaii"]
}

for person, places in favorite_places.items():
    print(f"{person}'s favorite places are:")
    for place in places:
        print(f"- {place}")