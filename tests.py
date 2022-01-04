from my_classes import Calculator
from my_functions import calculate_total_cost, fuel_calculator


try:
    print("test")
except (ValueError, TypeError) as err:
    print(err)
