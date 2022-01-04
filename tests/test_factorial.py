import unittest
from src.my_classes import Calculator

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculator()

    def test_negative(self):
        self.assertEqual(self.calc.factorial_recu(-1), False)

    def test_0(self):
        self.assertEqual(self.calc.factorial_recu(0), 1)

    def test_1(self):
        self.assertEqual(self.calc.factorial_recu(1), 1)

    def test_string_test(self):
        self.assertEqual(self.calc.factorial_recu("test"), False)

    def test_float_1_5(self):
        self.assertEqual(self.calc.factorial_recu(1.5), False)


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
