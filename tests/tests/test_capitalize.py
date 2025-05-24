from src.capitalize import capitalize


if capitalize("hello") != "Hello":
    raise Exception("функция работает неверно")

if capitalize("") != "":
    raise Exception("функция работает неверно")

print("all tests passed!")