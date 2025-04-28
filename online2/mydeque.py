"""
стек
deque
lifo
last in, first out
"""

"""

простой способ
list 
.append()
.pop()

правильный 
from collections import deque

"""
from collections import deque
stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')

top_element = stack.pop()
top_element2 = stack.pop()
top_element3 = stack.pop()


if stack:
    element = stack.pop()
else:
    print("пуст")
print(top_element)

stack = deque()

"""
push - поместить элемент на вершину .append(element)
pop - снять элемент с вершины 
peek - посмотреть на верхний элемент, не снимая его stack[-1]
"""
if not stack:
    print('стек пуст')

def reverse_string(s):
    stack = deque()
    for char in s:
        stack.append(char)

    reversed_s = ''
    while stack:
        reversed_s += stack.pop()

    return reversed_s

print(reverse_string('hello'))

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, item):
        self.container.append(item)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return not self.container

    def size(self):
        return len(self.container)


"""
очередь
deque
fifo
first in, first out
"""

"""

простой способ
list 
.append()
.pop(0)

правильный 
from collections import deque

"""
from collections import deque
queue = deque()
queue.append('1')
queue.append('2')
queue.append('3')

first = queue.popleft()
print(first)

"""
enqueue - добавить элемент в конец очереди .append(element)
dequeue - удалить элемент с начала очереди .popleft()
peek - посмотреть на первый элемент, не снимая его stack[0]
"""
if queue:
    first = queue[0]
else:
    print('очередь пуста')

if not queue:
    print("пусто")

size = len(queue)

def serve_customers(customers):
    queue = deque(customers)
    while queue:
        customer = queue.popleft()
        print(f'обслуживается {customer}')

customers_list = ['alice', 'bob', 'joe']
serve_customers(customers_list)

class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, item):
        self.container.append(item)

    def dequeue(self):
        return self.container.popleft()

    def peek(self):
        return self.container[0]

    def is_empty(self):
        return not self.container

    def size(self):
        return len(self.container)

q = Queue()
q.enqueue('alice')
q.enqueue('bob')
print(q.dequeue())
print(q.peek())
print(q.size())

"""
deque
double-ended queue
очередь с двумя концами
"""
mydeque = deque()
mydeque.append("A")
mydeque.appendleft("B") # добавление элемента в начало
mydeque.pop()
mydeque.popleft()
first_element = mydeque[0]
last_element = mydeque[-1]
length = len(mydeque)
if not mydeque:
    print('пусто')
mydeque.clear()

mydeque.extend(['C', "D", 'E']) # добавляет в конец
mydeque.extendleft(["X", "Y"]) # в начало в обратном порядке
mydeque.rotate(1) # все элементы сдвигаются вправо на 1
mydeque.rotate(-1) # все элементы сдвигаются влево на 1

log_queue = deque(maxlen=3)
log_queue.append('log1')
log_queue.append('log2')
log_queue.append('log3')
print(log_queue)
log_queue.append('log4')
print(log_queue)
"""
O()
                    list deque
добавление в конец   1     1
удаление с конца     1     1
добавление в начало  n     1
удаление с начала    n     1
доступ по индексу    1     n
"""

"""
fifi заказы от клиентов
срочный заказ - в начало очереди

add_order(order) - добавить обычный заказ в конец очереди
add_priority_oder(order) - начало
server_order() - обслужить
show_orders() - показать все заказы

учесть пустоту
"""