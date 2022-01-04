import unittest
from src.my_functions import fuel_calculator


class TestFuel(unittest.TestCase):

    def test_12(self):
        self.assertEqual(fuel_calculator(12), 2)

    def test_100756(self):
        self.assertEqual(fuel_calculator(100756), 33583)

    def test_string_12(self):
        self.assertEqual(fuel_calculator("12"), 2)

    def test_string_text(self):
        self.assertEqual(fuel_calculator("text"), False)

    def test_negative_value(self):
        self.assertEqual(fuel_calculator(-1), False)

    def test_zero(self):
        self.assertEqual(fuel_calculator(0), False)

    def test_1(self):
        self.assertEqual(fuel_calculator(1), 1)


if __name__ == "__main__":
    unittest.main()
