import time

from my_functions import factorial_recu, factorial_loop


class Animal:

    def __init__(self, type):
        self.type = type

    def make_a_sound(self):
        if self.type == "cat":
            print("meow")
        elif self.type == "dog":
            print("woof")
        else:
            print("no such animal")


class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        try:
            return a / b
        except (ZeroDivisionError, TypeError) as err:
            print(err)
            return False

    def factorial_recu(self, n):
        factorial_recu(n)

    def factorial_loop(self, n):
        factorial_loop(n)


if __name__ == "__main__":
    calc = Calculator()
    calc.div(1, 1)

    Calculator.add(1, 2)

    start_time = time.time()
    print(calc.factorial_loop(200))
    print(time.time() - start_time)
    start_time = time.time()
    print(calc.factorial_recu(200))
    print(time.time() - start_time)
