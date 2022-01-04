def square(number):
    result = number ** 2
    return result


def fuel_calculator(mass):
    try:
        mass = int(mass)
    except ValueError:
        return False
    if mass <= 0:
        return False
    elif mass < 9:
        return 1
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


def factorial_recu(n):
    if not isinstance(n, int):
        return False
    if n in [0, 1]:
        return 1
    elif n > 1:
        return n * factorial_recu(n - 1)
    else:
        return False


def factorial_loop(n):
    result = 1
    if n in [0, 1]:
        return 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    assert calculate_total_cost("Nicosia") == 4060, "Wrong city"
    print(calculate_total_cost("Nicosia"))
