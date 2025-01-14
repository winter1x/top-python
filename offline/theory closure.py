
"""

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)

result = closure(5)
print(result)

def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
counter1 = counter()
print(counter1())
print(counter1())
print(counter1())

def multiplier(n):
    def multiply(x):
        return  x * n
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(5))
print(triple(5))
"""
"""
def возвращает словарь счетчика с методами
+1
-1
текущее
сброс к начальному
история изменений
откат к предыдущему
"""

def smart_counter(initial_value=0):
    value = initial_value
    history_list = [initial_value]

    def increment():
        nonlocal value
        pass

    def decrement():
        nonlocal value
        value -= 1
        history_list.append(value)
    def get_value():
        return value
    def history():
        return history_list
    def undo():
        nonlocal value
        if len(history_list) > 1:
            history_list.pop()
            value = history_list[-1]
    return {
        "increment": increment,
        "decrement": decrement,
        "get_value": get_value,
        #reset
        "history": history,
        "undo": undo,
    }

counter = smart_counter(5)
counter['history']()
counter['undo']()
counter['decrement']()
