try:
    print("test")
except (ValueError, TypeError) as err:
    print(err)
