var_1 = True

if var_1 == 1 or var_1 == 2:
    print(True)
elif var_1 == 0:
    pass
else:
    pass

if var_1 in [1, 2]:
    print(True)

animal = {
    "type": "cat"
}

if "cat" in animal.values():
    print("You have home animal")

destination = "Chartum"

destinations = {
    "Nicosia": 1980,
    "Reykjavik": 2900,
    "Chartum": None
}

if destination in destinations:
    distance = destinations[destination]

    if distance:
        cost = 0
        if distance >= 2000:
            cost = 2 * distance
        elif 2000 > distance > 0:
            cost = 2 * distance + 100
        print(f"Total price is {cost}")
    else:
        print("No such destination")
else:
    print("No such destination")
