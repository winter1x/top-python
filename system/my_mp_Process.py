"""
GIL

Process - отдельный процесс
Queue - очередь (IPC) (FIFO) (Pipe, Lock, Semaphore, Thread)
    не используем когда
    процессы должны параллельно менять общую структуру
    когда объем данных достаточно большой
Pipe - канал
Pool - для работы с группой процессов
Value, Array, Manager - механизмы для общего доступа к данным между процессами
"""

from multiprocessing import Process
import time

def say_hello():
    print()
    print("я работаю в отдельном процессе")
    time.sleep(1)
    print("конец")
    print()

def print_square(x):
    print("квадрат числа {0} равен {1}".format(x, x*x))

def show_info():
    from multiprocessing import current_process
    print("текущий процесс", current_process().name)
    print("идентификатор процесса", current_process().pid)

class MyProcess(Process):
    def __init__(self, text):
        super().__init__()
        self.text = text

    def run(self):
        print(f"процесс получил {self.text}")

def worker(n):
    print(f"процесс {n} начал работу")
    time.sleep(5)
    print(f"процесс {n} закончил работу")

"""
создан (после p = Process(...))
запущен (после p.start())
ожидает завершения / ожидаемый (после p.join() - блокирует, пока не завершится)
завершен (после завршения функции)
"""


    
"""
запуск 5 процессов, работа через sleep
логирование

каждый процесс получает разное/случайное [1-5]c. время работы
использовать args
использовать join
"""
# from multiprocessing import Process
# import time

def sleeper(seconds, process_number):
    print(f"[{process_number}] Сон {seconds} секунд...")
    time.sleep(seconds)
    print(f"[{process_number}] Время проснулся!")

# if __name__ == '__main__':
#     delays = [3, 2, 4, 1, 5]
#     processes = []

#     for i, delay in enumerate(delays, start=1):
#         p = Process(target=sleeper, args=(delay, i))
#         processes.append(p)
#         print(f"[{i}] Процесс запущен!")
#         p.start()
    
#     for p in processes:
#         p.join()

#     print("Все процессы завершены!")
    
# 4 параллельных процесса. Каждый находит сумму квадратов в диапазоне
# from multiprocessing import Process
# import time

def sum_of_squares(start, end):
    print(f"процесс считает сумму квадратов от {start} до {end}")
    t1 = time.time()
    result = sum(x * x for x in range(start, end + 1))
    t2 = time.time()
    print(f"сумма квадратов от {start} до {end} равна {result} (время работы {t2 - t1} сек)")

"""if __name__ == '__main__':
    ranges = [
        (1, 250_000),
        (250_001, 500_000),
        (500_001, 750_000),
        (750_001, 1_000_000)
    ]

    processes = []

    start_time = time.time()

    for r in ranges:
        p = Process(target=sum_of_squares, args=r)
        processes.append(p)
        print("процесс запущен для диапазона", r)
        p.start()

    for p in processes:
        p.join()

    print("все процессы завершены")
    print("общее время работы", time.time() - start_time)"""

# добавить в задание 2. Задать каждому процессу имя и показать
# имя процесса
# pid
# is_alive()
# start_time, end_time

from multiprocessing import current_process
# from multiprocessing import Process
# import time

def task_with_info(start, end):
    proc = current_process()
    print(f"{proc.name} {proc.pid} {proc.is_alive()}")
    t1 = time.time()
    total = sum(x * x for x in range(start, end + 1))
    t2 = time.time()
    print(f"{proc.name} завершился. Сумма {total} (время работы {t2 - t1:.2f} сек)")

"""if __name__ == '__main__':
    ranges = [
        (1, 250_000),
        (250_001, 500_000),
        (500_001, 750_000),
        (750_001, 1_000_000)
    ]

    processes = []

    for i, r in enumerate(ranges, start=1):
        p = Process(target=task_with_info, args=r, name=f"Процесс-{i}")
        processes.append(p)
        print("процесс запущен для диапазона", r)
        p.start()

    for p in processes:
        p.join()"""

"""
создать 3 процесса, которые считают сумму квадратов, но один из них должен выполняться слишком долго time.sleep(100)
через 2 секунды принудительно завешить этот процесс terminate()

два процесса успешно
один не успел
"""

# from multiprocessing import Process
# import time

def long_task(index):
    print(f"Задача {index} начата")
    if index == 2:
        print("Задача 2 долго выполняется")
        time.sleep(100)
    else:
        time.sleep(1)
    print(f"Задача {index} завершена")

"""if __name__ == '__main__':
    processes = []

    for i in range(1, 4):
        p = Process(target=long_task, args=(i,))
        processes.append(p)
        print(f"Запущена задача {i}")
        p.start()

    time.sleep(2)

    for p in processes:
        if p.is_alive():
            print(f"Прерываю процесс {p}")
            p.terminate()

    for p in processes:
        p.join()

    print("Все процессы завершены")"""


"""
создать класс SquareSumProcess, наследующий от класса Process
в классе SquareSumProcess переопределить метод run() с подсчетом суммы квадратов в диапазоне

у каждого процесса должен быть свой диапазон
логирование

"""

# from multiprocessing import Process
# import time

class SquareSumProcess(Process):
    def __init__(self, start, end, name=None):
        super().__init__(name=name)
        self.start_num = start
        self.end_num = end
    
    def run(self):
        print(f"{self.name}: процесс считает сумму квадратов от {self.start_num} до {self.end_num}")
        t1 = time.time()
        result = sum(x * x for x in range(self.start_num, self.end_num + 1))
        t2 = time.time()
        print(f"{self.name}: сумма квадратов от {self.start_num} до {self.end_num} равна {result} (время работы {t2 - t1} сек)")

"""if __name__ == '__main__':
    ranges = [
        (1, 250_000),
        (250_001, 500_000),
        (500_001, 750_000),
        (750_001, 1_000_000)
    ]

    processes = []

    for i, r in enumerate(ranges, start=1):
        p = SquareSumProcess(start=r[0], end=r[1], name=f"Процесс-{i}")
        processes.append(p)
        p.start()

    for p in processes:
        p.join()"""






#Queue - очередь (IPC) (FIFO)
from multiprocessing import Queue
q = Queue()
q = Queue(maxsize=5)

"""
методы
put(item) - добавляет элемент в очередь. Если очередь заполнена, то блокируется
get(timeout=5) - извлекает элемент из очереди (удаляет из очереди). Если очередь пуста, то блокируется
put_nowait(item) - добавляет элемент в очередь, если очередь не заполнена
get_nowait() - извлекает элемент из очереди (удаляет из очереди), если очередь не пуста
empty() - возвращает True, если очередь пуста
full() - возвращает True, если очередь заполнена (maxsize)
"""

q = Queue()
q.put("один")
# print(q.get())

def producer(q):
    for i in range(5):
        print(f"Производитель кладет {i}")
        q.put(i)
        time.sleep(0.5)

def consumer(q):
    while True:
        item = q.get()
        print(f"потребитель получил {item}")
        if item == 4:
            break 

"""if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()"""

#get(timeout=5) - извлекает элемент из очереди (удаляет из очереди). Если очередь пуста, то блокируется
from queue import Empty
"""
try:
    item = q.get_nowait()
except Empty:
    print("очередь пуста")"""


def producer(q):
    for i in range(3):
        print(f"Производитель кладет {i}")
        q.put(i)

def consumer(q):
    for _ in range(3):
        item = q.get()
        print(f"потребитель получил {item}")

"""if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()"""
    
#from queue import Empty
from queue import Full

q = Queue(maxsize=2)

"""try:
    q.put_nowait(1)
    q.put_nowait(2)
    q.put_nowait(3) # очередь заполнена
    q.put_nowait(4)
except Full:
    print("очередь заполнена")


try:
    print("извлечено", q.get_nowait()) 
    print("извлечено", q.get_nowait()) 
    print("извлечено", q.get_nowait())  # очередь пуста
    print("извлечено", q.get_nowait())
except Empty:
    print("очередь пуста")"""


"""print("очередь пуста?", q.empty())
print("очередь заполнена?", q.full())

q.put(1)
q.put(2)

print("очередь пуста?", q.empty())
print("очередь заполнена?", q.full())"""

q = Queue()
"""try:
    print('пробую извлечь элемент из очереди')
    item = q.get(timeout=1) # ждет максимум 1 сек
    print('извлекли элемент', item)
except Empty:
    print('не дождались ответа = очередь пуста')"""

def producer(q):
    for i in range(5):
        print(f"Производитель кладет {i}")
        q.put(i)
        time.sleep(0.3)

def consumer(q):
    while True:
        if not q.empty():
            val = q.get()
            print(f"Потребитель получил {val}")
            if val == 4:
                break
        else:
            print("очередь пуста, жду")
            time.sleep(0.1)

"""if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
"""

"""
Queue
реализовать в систему
1) один или несколько производителей, которые генерируют задания (случайные числа от 1 до 100)
2) один или несколько потребителей получают задания из очереди и выполняют их обработку (простое что-то)
"""

#from multiprocessing import Queue, Process, current_process
#import time
import random
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def producer(q, count):
    for _ in range(count):
        num = random.randint(1, 100)
        print(f"[{current_process().name}] Производитель создал задание {num}")
        q.put(num)
        time.sleep(random.uniform(0.1, 0.3))
    q.put(None)
    print(f"[{current_process().name}] Производитель отправил сигнал завершения")

def consumer(q):
    while True:
        num = q.get()
        if num is None:
            q.put(None)
            print(f"[{current_process().name}] Потребитель получил сигнал завершения")
            break
        result = is_prime(num)
        print(f"[{current_process().name}] Потребитель обработал задание {num}, результат {result}")

if __name__ == '__main__':
    q = Queue()
    producers = [
        Process(target=producer, args=(q, 10), name="Производитель 1"),
        Process(target=producer, args=(q, 10), name='Производитель 2'),
    ]

    consumers = [
        Process(target=consumer, args=(q,), name=f"Потребитель {i+1}")
        for i in range(3)
    ]

    for p in producers:
        p.start()

    for c in consumers:
        c.start()

    for p in producers:
        p.join()

    for c in consumers:
        c.join()
    
    print("Все процессы завершены")
    