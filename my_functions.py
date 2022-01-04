def square(number):
    result = number ** 2
    return result


def fuel_calculator(mass):
    return mass // 3 - 2


def calculate_total_cost(destination):
    destinations = {
        "Nicosia": 1980,
        "Reykjavik": 2900,
        "Chartum": None
    }

    if destination not in destinations:
        return False

    distance = destinations[destination]

    if not distance:
        return False

    cost = 0
    if distance >= 2000:
        cost = 2 * distance
    elif 2000 > distance > 0:
        cost = 2 * distance + 100
    return cost


if __name__ == "__main__":
    assert calculate_total_cost("Nicosia") == 4060, "Wrong city"
    print(calculate_total_cost("Nicosia"))
