from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)

print(stack.pop())
print(stack.pop())
print(stack.pop())

if not stack:
    print("Стек пуст")

"""
append(x)     добавляет элемент x в конец стека
pop()         удаляет и возвращает последний элемент стека
if not stack  проверка, пуст ли стек
clear()
stack[-1]     Peek Просмотр верхнего элемента
"""

"""
Дана строка, содержащая скобки различных типов: (), [], {}. 
Необходимо проверить, является ли скобочная последовательность корректной. 
Корректная последовательность означает, 
что каждой открывающей скобке соответствует закрывающая скобка того же типа, 
и скобки правильно вложены друг в друга.
"""

str1 = "()[]{}" # True
str2 = "([{}])" # True
str3 = "(]" # False
str4 = "([)]" # False

def is_valid_brackets(s):
    stack = []
    brackets_map = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in brackets_map.values():
            stack.append(char)
        elif char in brackets_map:
            if not stack or stack.pop() != brackets_map[char]:
                return False
    return not stack

print(is_valid_brackets(str1))
print(is_valid_brackets(str2))
print(is_valid_brackets(str3))
print(is_valid_brackets(str4))

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

if not queue:
    print("Очередь пуста")

"""
реализовать class структуру данных очередь
добавление элемента в очередь enqueue
удаление элемента из очереди dequeue
получение максимального элемента в очереди get_max
получение минимального элемента в очереди get_min

использовать deque 
"""

class SimpleMinMaxQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if not self.queue:
            return None
        return self.queue.popleft()

    def get_max(self):
        if not self.queue:
            return None
        return max(self.queue)

    def get_min(self):
        if not self.queue:
            return None
        return min(self.queue)

smq = SimpleMinMaxQueue()
smq.enqueue(3)
smq.enqueue(1)
smq.enqueue(5)
print(smq.get_max())
print(smq.get_min())
print()
smq.dequeue()
print(smq.get_max())
print(smq.get_min())
print()
smq.dequeue()
print(smq.get_max())
print(smq.get_min())
print()
smq.dequeue()
print(smq.get_max())
print(smq.get_min())
"""
добавление
append(x)
appendleft(x)

удаление
pop()
popleft()

методы
extend(iterable) — добавляет все элементы из итерируемого объекта в конец deque
extendleft(iterable) — добавляет все элементы из итерируемого объекта в начало deque (элементы добавляются в обратном порядке)
rotate(n) — циклически сдвигает элементы deque на n шагов. Если n положительное, сдвиг происходит вправо, если отрицательное — влево
clear()  полностью очистить
count(x)  возвращает количество элементов, равных x
remove(x)  удаляет первый найденный элемент, равный x

свойство
maxlen  максимальный размер deque (если задан). Если при добавлении элементов размер превышает maxlen, элементы с противоположного конца автоматически удаляются
"""
