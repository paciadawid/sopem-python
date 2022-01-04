a_int = 100000000000000000000000000000000000000000000000

a_float = 1.0

print(1 / 2)
print(1 // 2)

a_str = "Test"
print(a_str[0])
print(a_str[-1])
print(a_str[1:3])

a_set = {1, 2, 2}
a_set.add(3)
print(a_set)

a_list = [1, 2.0, "2"]
a_list.append(1)
print(a_list[-1])
print(a_list.pop(1))

a_tuple = (1, 2.0, "2")
# del a_tuple[1]

a_dict = {
    "key": "value",
    1: 2,
    1.0: 2
}
print(a_dict[1])
print(a_dict["key"])

a_bool = True
a_none = None

if a_bool:
    print("True")

a_test = []  # (), {}, ""

if a_test:
    print("True")
else:
    print("False")

python = {
    "animal": "cat",
    "age": 3,
    "weight": 4.1,
    "colours": ("white", "black"),
    "toys": ["mouse", "ball", "feet"],
    "if_hungry": True
}

print(python)
print(f'My cat age is {python["age"]} \'')

test_string = "//div[@id={current_id}]"
print(test_string.format(current_id=1))
