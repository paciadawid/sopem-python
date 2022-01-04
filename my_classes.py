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


calc = Calculator()
calc.div(1, 1)

Calculator.add(1, 2)
