import random
import string

def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

def random_list(size=10, min_val=0, max_val=100):
    return [random.randint(min_val, max_val) for _ in range(size)]

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def reverse_string(s):
    return s[::-1]

def is_even(n):
    return n % 2 == 0

class Nonsense:
    def __init__(self):
        self.data = {random_string(): random_list() for _ in range(10)}

    def shuffle_keys(self):
        keys = list(self.data.keys())
        random.shuffle(keys)
        self.data = {key: self.data[key] for key in keys}

    def mutate_values(self):
        for key in self.data:
            self.data[key] = [multiply_numbers(val, random.choice([-1, 1])) for val in self.data[key]]

    def filter_data(self):
        self.data = {k: v for k, v in self.data.items() if is_even(sum(v))}

    def nonsense_operation(self):
        temp = {}
        for key in self.data:
            temp[reverse_string(key)] = [x**2 if is_even(x) else x**3 for x in self.data[key]]
        self.data = temp

    def display(self):
        for key, value in self.data.items():
            print(f"{key}: {value}")

print(add_numbers(5, 7))
print(multiply_numbers(3, 4))
print(reverse_string("Hello, World!"))
print(is_even(10))
print(is_even(7))

n = Nonsense()
n.shuffle_keys()
n.mutate_values()
n.filter_data()
n.nonsense_operation()
n.display()
