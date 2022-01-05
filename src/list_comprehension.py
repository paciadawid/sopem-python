# squares from values 1 to 10
import random

squares = [x ** 2 for x in range(1, 11)]
# create a list of all 2-digit odd numbers
odd_numbers = [x for x in range(10, 100) if x % 2]
# list/set of vowels from text “i like pancakes”
letters = {letter for letter in "i like pancakes" if letter in "aeiouy"}
# create a 3x3 matrix (of random values from 0 to 9)
matrix = [[random.randint(0, 9) for _ in range(3)] for _ in range(3)]
print(matrix)

a = [1, 2, 3, 4, 5]

b = [x + 1 for x in a if x > 2]

with open("data.txt", "rb") as file:
    my_data = [int(line.strip()) for line in file.readlines()]

text = ["test", "test", "test"]
print(" ".join(text))

a = 10
b = bin(a)
print(b[2:])
