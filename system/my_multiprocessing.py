"""
multiprocessing - для работы с процессами
    если задача вычислительно тяжелая 

time.perf_counter() - время в секундах

GIL - Global Interpreter Lock

Process - отдельный/независимый процесс
    .start() - запуск процесса
    .join() - ожидание завершения процесса
    args=() - аргументы запуска процесса
    .pid PID - идентификатор процесса
    .name - имя процесса
    .is_alive() - проверка на активность процесса (не безопасно)
    .terminate() - резкое завершение процесса принудительно
    значения не пересекаются между процессами напрямую
    if __name__ == '__main__':

Queue - потокобезопасная очередь (IPC - inter-process communication) (FIFO) (Pipe, Lock, Semaphore, Thread, pickle)
    q = Queue() - очередь
    q = Queue(maxsize=5) - очередь с ограничением на размер
    put(item) - добавляет элемент в очередь. Если очередь заполнена, то блокируется
    get(timeout=5) - извлекает элемент из очереди (удаляет из очереди). Если очередь пуста, то блокируется
    put_nowait(item) - добавляет элемент в очередь, если очередь не заполнена
    get_nowait() - извлекает элемент из очереди (удаляет из очереди), если очередь не пуста
    empty() - возвращает True, если очередь пуста (небезопасно)
    full() - возвращает True, если очередь заполнена (maxsize) (небезопасно)

    используем когда
    очередь задач (пул задач) с несколькими исполнителями
    продюсер-консьюмер
    логирование 
    передача результата

    не используем когда
    процессы должны параллельно менять общую структуру
    когда объем данных достаточно большой

JoinableQueue
    task_done() - вручную вызывать, когда задача выполнена
    join() - ожидать завершения всех задач

    используем когда:
    построение пайплайнов
    пул процессов
    с лентами задач
    в реализациях MapReduce
    много задач
    нужно убедиться что все задачи выполнены
    контроль порядка и завершения

Pipe - канал
    Pipe(duplex=False) - 1 канал

    conn = Connection()
    conn.send(obj) - отправить объект в другой конец канала. должен быть pickle - сериализуемый
    conn.recv() - получить объект из канала
    conn.close() - закрыть канал
    conn.fileno() - вернуть дескриптор файла канала
    conn.poll(timeout=None) - проверить, доступен ли объект в канале в течение заданного времени

    не используем когда:
    больше 2 процесса
    очередь задач с несколькими исполнителями
    нужна потокобезопасность
    когда объем данных достаточно большой

    ограничения:
    .recv(), .send() - блокируют поток

Pool - для работы с группой процессов (Process, Queue). Повторно использовать группу рабочих процессов
    map(func, iterable) - многопроцессная версия map
    starmap - аналогично map, но с возможностью передачи нескольких аргументов в функцию
    apply(func, args) - Вызывает func(*args). Блокирует выполнение до завершения работы процесса. 
    apply_async(func, args) - Вызывает func(*args) асинхронно, не блокируя выполнение. Возвращает AsyncResult
    AsyncResult - объект, который содержит результат работы функции
    imap(func, iterable) - аналогичен map(), но возвращает результаты по мере их готовности. Возвращает итератор
    close() - закрывает доступ к очереди для добавления новых элементов
    join() - ждет завершения всех процессов в пуле

Value, Array, Manager - механизмы для общего доступа к данным между процессами

ProcessPoolExecutor - многопроцессорная очередь задач CPU

Lock - блокировка, одна задача выполняется одновременно
RLock - рекурсивная блокировка

активное ожидание busy waiting
while not queue.empty(): - антипаттерн
    item = queue.get()
(-)
нагрузка на CPU
нет гарантии точности
проблемы с масштабированием

конкурентная среда - одновременная работа/обращение к общим ресурсам
race condition условная гонка
deadlock взаимные блокировки
starvation голодание
низкий приоритет (инверсия)
"""





from multiprocessing import Process
import time

def worker(n):
    print(f"процесс {n} начал работу")
    time.sleep(5)
    x = 2
    print(f"процесс {n} закончил работу")

"""
p1 = Process(target=worker)
p1.start()
p1.join()

создан (после p = Process(...))
запущен (после p.start())
ожидает завершения / ожидаемый (после p.join() - блокирует, пока не завершится)
завершен (после завршения функции)
"""


from multiprocessing import Queue

def producer(queue):
    queue.put("Привет, я из процесса")

def consumer(queue):
    msg = queue.get()
    print(f"получено: {msg}")

"""
q = Queue()
p1 = Process(target=producer, args=(q,))
p2 = Process(target=consumer, args=(q,))

p1.start()
p2.start()

p1.join()
p2.join()
"""


from multiprocessing import Pool

def square(x):
    return x * x

# with Pool(4) as pool:
#     results = pool.map(square, range(10))
#     print(results)


"""def task(arg):
    pass

if __name__ == '__main__':
    processes = []
    for i in range(4):
        p = Process(target=task, args=(i,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()"""


def say_hello():
    print()
    print("я работаю в отдельном процессе")
    time.sleep(1)
    print("конец")
    print()

# if __name__ == '__main__':
#     p = Process(target=say_hello)
#     p.start()
#     p.join()


def print_square(x):
    print("квадрат числа {0} равен {1}".format(x, x*x))


# if __name__ == '__main__':
#     p = Process(target=print_square, args=(5,))
#     p.start()
#     p.join()

def show_info():
    from multiprocessing import current_process
    print("текущий процесс", current_process().name)
    print("идентификатор процесса", current_process().pid)

# if __name__ == '__main__':
#     p = Process(target=show_info, name="Процесс-1")
#     p.start()
#     p.join()


class MyProcess(Process):
    def __init__(self, text):
        super().__init__()
        self.text = text

    def run(self):
        print(f"процесс получил текст {self.text}")

# if __name__ == '__main__':
#     p = MyProcess("Процесс-1")
#     p.start()
#     #завершен
#     p.join()

    
def worker2(n):
    print(f"процесс {n} начал работу")
    time.sleep(1)
    print(f"процесс {n} закончил работу")

# if __name__ == '__main__':
#     processes = []
#     for i in range(4):
#         p = Process(target=worker2, args=(i,))
#         p.start()
#         processes.append(p)

#     for p in processes:
#         p.join()

"""

запуск 5 процессов, работа через sleep
логирование

каждый процесс получает разное/случайное [1-5]c. время работы
использовать Process
использовать args=
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

# if __name__ == '__main__':
#     ranges = [
#         (1, 250_000),
#         (250_001, 500_000),
#         (500_001, 750_000),
#         (750_001, 1_000_000)
#     ]

#     processes = []

#     start_time = time.time()

#     for r in ranges:
#         p = Process(target=sum_of_squares, args=r)
#         processes.append(p)
#         print("процесс запущен для диапазона", r)
#         p.start()

#     for p in processes:
#         p.join()

#     print("все процессы завершены")
#     print("общее время работы", time.time() - start_time)

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

# if __name__ == '__main__':
#     ranges = [
#         (1, 250_000),
#         (250_001, 500_000),
#         (500_001, 750_000),
#         (750_001, 1_000_000)
#     ]

#     processes = []

#     for i, r in enumerate(ranges, start=1):
#         p = Process(target=task_with_info, args=r, name=f"Процесс-{i}")
#         processes.append(p)
#         print("процесс запущен для диапазона", r)
#         p.start()

#     for p in processes:
#         p.join()

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

# if __name__ == '__main__':
#     processes = []

#     for i in range(1, 4):
#         p = Process(target=long_task, args=(i,))
#         processes.append(p)
#         print(f"Запущена задача {i}")
#         p.start()

#     time.sleep(2)

#     for p in processes:
#         if p.is_alive():
#             print(f"Прерываю процесс {p}")
#             p.terminate()

#     for p in processes:
#         p.join()

#     print("Все процессы завершены")


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

# if __name__ == '__main__':
#     ranges = [
#         (1, 250_000),
#         (250_001, 500_000),
#         (500_001, 750_000),
#         (750_001, 1_000_000)
#     ]

#     processes = []

#     for i, r in enumerate(ranges, start=1):
#         p = SquareSumProcess(start=r[0], end=r[1], name=f"Процесс-{i}")
#         processes.append(p)
#         p.start()

#     for p in processes:
#         p.join()

"""
1
запускать два процесса
первый считает от 1 до 10, печатает числа
второй считает от 10 до 1, печатает числа
каждый выводит результат с задержкой в 0.5 сек
"""
# from multiprocessing import Process
# import time

def count_up():
    for i in range(1, 11):
        print(f"Счет вверх: {i}")
        time.sleep(0.5)

def count_down():
    for i in range(10, 0, -1):
        print(f"Счет вниз: {i}")
        time.sleep(0.5)

# if __name__ == '__main__':
#     p1 = Process(target=count_up)
#     p2 = Process(target=count_down)

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()
"""
2
список из 5 чисел, два процесса
первый вычисляет квадраты чисел и печатает их
второй вычисляет кубы чисел и печатает их
"""
# from multiprocessing import Process

def squares(numbers):
    for n in numbers:
        print(f"Квадрат числа {n} равен {n ** 2}")

def cubes(numbers):
    for n in numbers:
        print(f"Куб числа {n} равен {n ** 3}")

# if __name__ == '__main__':
#     numbers = [1, 2, 3, 4, 5]

#     p1 = Process(target=squares, args=(numbers,))
#     p2 = Process(target=cubes, args=(numbers,))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()
"""
3
два процесса
первый "таймер", каждую секунду печатает, сколько времени прошло
второй "работа", который за 5 секунд выполняет задачу (например сумма от 1 до 10кк)
"""
# from multiprocessing import Process
# import time

def timer():
    sec = 0
    while True:
        time.sleep(1)
        sec += 1
        print(f"Прошло {sec} секунд")

def heavy_work():
    s = 0
    for i in range(1, 10_000_000):
        s += i
    print(f"Сумма от 1 до 10_000_000 равна {s}")

# if __name__ == '__main__':
#     t = Process(target=timer)
#     w = Process(target=heavy_work)

#     t.start()
#     w.start()

#     w.join()
#     t.terminate()
#     print("Работа завершена")
"""
4
запускает три процесса, каждый из которых проверяет, есть ли простые числа в своем диапазоне
1 от 2 до 10000
2 от 10001 до 20000
3 от 20001 до 30000
каждый процесс выводит количество найденных простых чисел
"""
# from multiprocessing import Process
def is_prime(n):
    if n <= 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(start, end):
    count = 0
    for i in range(start, end + 1):
        if is_prime(i):
            count += 1
    print(f"Процесс в диапазоне {start}-{end} нашел {count} простых чисел")

# if __name__ == '__main__':
#     p1 = Process(target=count_primes, args=(2, 10000))
#     p2 = Process(target=count_primes, args=(10001, 20000))
#     p3 = Process(target=count_primes, args=(20001, 30000))

#     p1.start()
#     p2.start()
#     p3.start()

#     p1.join()
#     p2.join()
#     p3.join()
"""
5
два процесса, бесконечный цикл, каждый печатает что работает
главный процесс ждет 3 секунды и завершает 1 процесс, через еще 3 секунды завершает второй
"""
# from multiprocessing import Process
# import time

def worker3(name):
    while True:
        print(f"Процесс {name} работает")
        time.sleep(1)

# if __name__ == '__main__':
#     p1 = Process(target=worker3, args=("A",))
#     p2 = Process(target=worker3, args=("B",))

#     p1.start()
#     p2.start()

#     time.sleep(3)
#     print("Завершаю процесс A")
#     p1.terminate()

#     time.sleep(3)
#     print("Завершаю процесс B")
#     p2.terminate()


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

def producer1(q):
    for i in range(5):
        print(f"Производитель кладет {i}")
        q.put(i)
        time.sleep(0.5)

def consumer1(q):
    while True:
        item = q.get()
        print(f"потребитель получил {item}")
        if item == 4:
            break 

# if __name__ == '__main__':
#     q = Queue()
#     p1 = Process(target=producer1, args=(q,))
#     p2 = Process(target=consumer1, args=(q,))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#get(timeout=5) - извлекает элемент из очереди (удаляет из очереди). Если очередь пуста, то блокируется
from queue import Empty
"""
try:
    item = q.get_nowait()
except Empty:
    print("очередь пуста")"""


def producer2(q):
    for i in range(3):
        print(f"Производитель кладет {i}")
        q.put(i)

def consumer2(q):
    for _ in range(3):
        item = q.get()
        print(f"потребитель получил {item}")

# if __name__ == '__main__':
#     q = Queue()
#     p1 = Process(target=producer2, args=(q,))
#     p2 = Process(target=consumer2, args=(q,))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()
    
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

def is_prime3(n):
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

def producer3(q, count):
    for _ in range(count):
        num = random.randint(1, 100)
        print(f"[{current_process().name}] Производитель создал задание {num}")
        q.put(num)
        time.sleep(random.uniform(0.1, 0.3))
    q.put(None)
    print(f"[{current_process().name}] Производитель отправил сигнал завершения")

def consumer3(q):
    while True:
        num = q.get()
        if num is None:
            q.put(None)
            print(f"[{current_process().name}] Потребитель получил сигнал завершения")
            break
        result = is_prime3(num)
        print(f"[{current_process().name}] Потребитель обработал задание {num}, результат {result}")

# if __name__ == '__main__':
#     q = Queue()
#     producers = [
#         Process(target=producer3, args=(q, 10), name="Производитель 1"),
#         Process(target=producer3, args=(q, 10), name='Производитель 2'),
#     ]

#     consumers = [
#         Process(target=consumer3, args=(q,), name=f"Потребитель {i+1}")
#         for i in range(3)
#     ]

#     for p in producers:
#         p.start()

#     for c in consumers:
#         c.start()

#     for p in producers:
#         p.join()

#     for c in consumers:
#         c.join()
    
#     print("Все процессы завершены")

"""
производитель кладет от 1 до 10
потребитель берет числа из очереди и печатает их квадрат
когда производитель закончит, кладет STOP
"""
#from multiprocessing import Queue, Process
#import time

def producer4(queue):
    for i in range(1, 11):
        print(f"Производитель кладет {i}")
        queue.put(i)
        time.sleep(0.3)

    queue.put("STOP")
    print("Производитель закончил")

def consumer4(queue):
    while True:
        item = queue.get()
        if item == "STOP":
            print("Потребитель закончил")
            break
        else:
            print(f"Потребитель получил {item} и печатает квадрат {item ** 2}")

# if __name__ == '__main__':
#     queue = Queue()
#     p = Process(target=producer4, args=(queue,))
#     c = Process(target=consumer4, args=(queue,))

#     p.start()
#     c.start()

#     p.join()
#     c.join()

#     q.close()
#     q.join_thread()

def worker4(data, queue):
    result = sum(x ** 2 for x in data)
    queue.put(result)

# if __name__ == '__main__':
#     q = Queue()
#     chunks = [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]

#     processes = []

#     for chunk in chunks:
#         p = Process(target=worker4, args=(chunk, q))
#         processes.append(p)
#         p.start()

#     results = []
#     for _ in range(len(processes)):
#         result = q.get(timeout=5)
#         #if result is None:
#             #завершения += 1
#         results.append(result)

#     # from queue import Empty
#     # try:
#     #     item = q.get_nowait()
#     # except Empty:
#     #     print("Queue is empty")


#     for p in processes:
#         p.join()

#     print(results)
#     print(sum(results))


def worker(q):
    time.sleep(1)
    q.get()

"""if __name__ == '__main__':
    q = Queue()
    p = Process(target=worker, args=(q,))
    p.start()

    if not q.empty():
        q.get()
    item = queue.get(timeout=5)
    p.join()"""


#конкурентный доступ к переменной
import threading

counter = 0

def increment():
    global counter
    for _ in range(10):
        time.sleep(0.001)
        counter += 1

# if __name__ == '__main__':

#     t1 = threading.Thread(target=increment)
#     t2 = threading.Thread(target=increment)

#     t1.start()
#     t2.start()

#     t1.join()
#     t2.join()

#     print(counter)

counter = 0
lock = threading.Lock()
def increment():
    global counter
    for _ in range(10):
        with lock:
            counter += 1

# if __name__ == '__main__':
#     t1 = threading.Thread(target=increment)
#     t2 = threading.Thread(target=increment)

#     t1.start()
#     t2.start()

#     t1.join()
#     t2.join()

#     print(counter)


from multiprocessing import Pipe
"""
conn.send(obj) - отправить объект в другой конец канала
conn.recv() - получить объект из канала
conn.close() - закрыть канал
conn.fileno() - вернуть дескриптор файла канала
conn.poll(timeout=None) - проверить, доступен ли объект в канале в течение заданного времени
"""
def worker5(conn):
    conn.send('привет от дочернего процесса')
    conn.close()

# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe(duplex=False)

#     p = Process(target=worker5, args=(child_conn,))
#     p.start()

#     if parent_conn.poll(1):
#         print(parent_conn.recv())
#     else:
#         print('нет данных')
#     p.join()

"""
if parent_conn.poll(1):
    print(parent_conn.recv())
else:
    print('нет данных')
"""

def child2(conn):
    msg = conn.recv()
    print(f'получено сообщение: {msg}')
    conn.send('привет от дочернего процесса')
    conn.close()

# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()
#     p = Process(target=child2, args=(child_conn,))
#     p.start()

#     parent_conn.send('привет от родительского процесса')
#     msg = parent_conn.recv()
#     print(f'получено сообщение main: {msg}')

#     p.join()

"""
Pipe
1 создать дочерний процесс, отправляющий родительскому дату время datetime.now()
родитель получает выводит

2 диалог. Родитель отправляет число, дочерний выводит его в квадрате, родитель печатет результат

3 доделать 2, проверка poll() 3 секунды
"""

#from multiprocessing import Pipe, Process
from datetime import datetime


def send_datetime(conn):
    now = datetime.now()
    conn.send(str(now)) 
    conn.close()


# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()

#     p = Process(target=send_datetime, args=(child_conn,))
#     p.start()

#     message = parent_conn.recv()
#     print(f"Получено сообщение от дочернего процесса: {message}")

#     p.join()

def square_worker(conn):
    number = conn.recv()
    result = number ** 2
    conn.send(result)
    conn.close()

# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()

#     p = Process(target=square_worker, args=(child_conn,))
#     p.start()

#     number_to_send = 7
#     print(f"Отправка числа {number_to_send} в дочерний процесс")
#     parent_conn.send(number_to_send)
    
#     result = parent_conn.recv()
#     print(f"Получен результат: {result}")

#     p.join()

#import time

def delayed_square_worker(conn):
    number = conn.recv()
    time.sleep(2)
    result = number ** 2
    conn.send(result)
    conn.close()

# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()

#     p = Process(target=delayed_square_worker, args=(child_conn,))
#     p.start()

#     number_to_send = 8
#     print(f"Отправка числа {number_to_send} в дочерний процесс")
#     parent_conn.send(number_to_send)

#     if parent_conn.poll(3):
#         result = parent_conn.recv()
#         print(f"Получен результат: {result}")
#     else:
#         print("Время ожидания истекло")

#     p.join()

"""
отправитель отправляет от 1 до 5 
приемник получает через Pipe и печатет их квадрат
когда отправитель закончит, он отправит специальное сообщение "STOP" и применик завершит работу
"""
#from multiprocessing import Pipe, Process
#import time

def sender2(conn):
    for i in range(1, 6):
        print(f"Отправка числа {i} в дочерний процесс")
        conn.send(i)
        time.sleep(0.5)

    conn.send("STOP")
    conn.close()
    print("Отправитель завершил работу")

def receiver2(conn):
    while True:
        data = conn.recv()
        if data == "STOP":
            break
        print(f"Полученное число: {data}, квадрат: {data ** 2}")
    conn.close()
    print("Приемник завершил работу")

# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()

#     s = Process(target=sender2, args=(parent_conn,))
#     r = Process(target=receiver2, args=(child_conn,))

#     s.start()
#     r.start()

#     s.join()
#     r.join()

#from multiprocessing import Queue, Process
#import time

# от нескольких в родительский

def worker(name, q):   
    msg = f"Привет, я процесс {name}!"
    time.sleep(1)
    q.put(msg)

"""if __name__ == '__main__':
    queue = Queue()
    processes = [
        Process(target=worker, args=(f"процесс {i}", queue))
        for i in range(1, 3)
    ]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    for _ in range(len(processes)):
        print(queue.get())"""

# производитель и потребитель

#import random

def producer(q):
    for i in range(5):
        value = random.randint(1, 100)
        print(f"Производитель добавил элемент {value}")
        q.put(value)
        time.sleep(1)

def consumer(q):
    for _ in range(5):
        value = q.get()
        print(f"Потребитель получил элемент {value}")
        time.sleep(1)

"""if __name__ == '__main__':
    queue = Queue()

    p1 = Process(target=producer, args=(queue,))
    p2 = Process(target=consumer, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    """
# очередь для сбора результатов параллельных вычислений
#import math

def calc_factorial(n, q):
    result = math.factorial(n)
    q.put((n, result))

"""if __name__ == '__main__':
    numbers = [5, 10, 15, 20]
    queue = Queue()
    processes = []

    for n in numbers:
        p = Process(target=calc_factorial, args=(n, queue))
        processes.append(p)
        print(f"запустили процесс {p.name} для вычисления факториала {n}")
        p.start()

    for p in processes:
        p.join()

    for _ in range(len(numbers)):
        n, result = queue.get()
        print(f"Факториал числа {n} равен {result}")"""

# maxsize

def producer(q):
    for i in range(5):
        print(f"Производитель пытается добавить элемент {i}")
        q.put(i)
        print(f"Производитель добавил элемент {i}")
        time.sleep(0.5)

def consumer(q):
    time.sleep(1)
    while True:
        value = q.get()
        print(f"Потребитель получил элемент {value}")
        time.sleep(1)

"""if __name__ == '__main__':
    queue = Queue(maxsize=2)

    p1 = Process(target=producer, args=(queue,))
    p2 = Process(target=consumer, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.terminate()"""
    

# конкрунция за очередь
#from multiprocessing import Queue, Process, current_process
#import time

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Потребитель {current_process().name} получил элемент {item}")
        time.sleep(0.3)

"""if __name__ == '__main__':
    queue = Queue()
    for i in range(10):
        queue.put(i)

    num_consumers = 2
    for _ in range(num_consumers):
        queue.put(None)

    p1 = Process(target=consumer, args=(queue,), name="Потребитель 1")
    p2 = Process(target=consumer, args=(queue,), name="Потребитель 2")

    p1.start()
    p2.start()

    p1.join()
    p2.join()"""


# таймауты
#from multiprocessing import Queue, Process
#import time

def safe_get(q):
    try:
        itme = q.get(timeout=2)
        print(f"Получен элемент {item}")
    except Exception as e:
        print(f"ничего не получили: {type(e)}")

"""if __name__ == '__main__':
    queue = Queue()

    p = Process(target=safe_get, args=(queue,))
    p.start()
    p.join()"""


# from multiprocessing import Pipe, Process

# одностороння от дочерний к родителю

def child(conn):
    message = 'Привет от дочернего процесса!'
    conn.send(message)
    conn.close()

"""if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=child, args=(child_conn,))
    p.start()
    received_message = parent_conn.recv()
    print(f"Получено сообщение от дочернего процесса: {received_message}")
    p.join()"""

# двусторонняя от родителя к дочернему

def child(conn):
    number = conn.recv()
    result = number ** 2
    conn.send(result)
    conn.close()

"""if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=child, args=(child_conn,))
    p.start()
    parent_conn.send(5)
    result = parent_conn.recv()
    print(f"Результат: {result}")
    p.join()"""


#poll

def delayed_sender(conn):
    time.sleep(2)
    conn.send("Привет от дочернего процесса!")
    conn.close()

"""if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=delayed_sender, args=(child_conn,))
    p.start()
    print('ожидание 3 секунд...')
    if parent_conn.poll(3):
        received_message = parent_conn.recv()
        print(f"Получено сообщение от дочернего процесса: {received_message}")
    else:
        print("Время ожидания истекло")
    p.join()"""

# несколько сообщений от дочернего к родителю

def child(conn):
    for i in range(3):
        time.sleep(1)
        conn.send(f"Сообщение {i+1} от дочернего процесса")
    conn.send('конец')
    conn.close()

"""if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=child, args=(child_conn,))
    p.start()
    while True:
        message = parent_conn.recv()
        if message == 'конец':
            break
        print(f"Получено сообщение от дочернего процесса: {message}")
    p.join()"""

#структурированный обмен

def child(conn):
    data = {'name': 'Дочерний процесс', 'message': 'Привет от дочернего процесса!'}
    conn.send(data)
    conn.close()

"""if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=child, args=(child_conn,))
    p.start()

    data = parent_conn.recv()
    for key, value in data.items():
        print(f"{key}: {value}")
    p.join()"""

# чат между процессами

def child(conn):
    while True:
        question = conn.recv()
        if question.lower() == 'пока':
            conn.send('Пока!')
            break
        else:
            conn.send(f"вы сказали {question}")

"""if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=child, args=(child_conn,))
    p.start()

    for msg in ['Привет', 'Как дела?', 'Пока']:
        parent_conn.send(msg)
        answer = parent_conn.recv()
        print(f"ответ: {answer}")

    p.join()"""

# JoinableQueue
"""
task_done()
join()
"""
from multiprocessing import JoinableQueue

"""queue = JoinableQueue()

for i in range(10):
    queue.put(i)"""

def worker6(q):
    while True:
        item = q.get()
        if item is None:
            q.task_done()
            break
        print(f"Получен элемент {item}")
        time.sleep(0.3)
        q.task_done()
        
# if __name__ == '__main__':
#     queue = JoinableQueue()

#     processes = []
#     for _ in range(2):
#         p = Process(target=worker6, args=(queue,))
#         processes.append(p)
#         p.start()

#     for i in range(5):
#         queue.put(f"задача {i}")

#     for _ in processes:
#         queue.put(None)

#     queue.join()

#     for p in processes:
#         p.join()
        
#     print("Все задания выполнены")


"""item = queue.get()
try:
    обработка(item)
finally:
    queue.task_done()"""


"""
1 создать
заполнить 5 задачами
2 воркера 

2 доделать 1
каждая третья задача ValueError 
try/finally

3 расширить 1
добавить вторую обычную Queue, в которую воркеры будут добавлять результаты
после join показать все результаты
"""

def worker(q):
    while True:
        task = q.get()
        if task is None:
            q.task_done()
            break
        print(f'{task} - выполняется')
        time.sleep(1)
        print(f'{task} - выполнено')
        q.task_done()

"""if __name__ == '__main__':
    q = JoinableQueue()

    workers = [
        Process(target=worker, args=(q,))
        for _ in range(2)
    ]
    for w in workers:
        w.start()

    for i in range(5):
        q.put(f'задача {i}')

    for _ in workers:
        q.put(None)

    q.join()
    print('Все задачи выполнены')"""

def worker(q):
    while True:
        task = q.get()
        try:
            if task is None:
                break
            if task.endswith('3'):
                raise ValueError
            print(f'{task} - выполняется')
            time.sleep(1)
            print(f'{task} - выполнено')
        except Exception as e:
            print(f'ошибка в задаче {task}: {type(e)}')
        finally:
            q.task_done()
            
"""if __name__ == '__main__':
    q = JoinableQueue()

    workers = [
        Process(target=worker, args=(q,))
        for _ in range(2)
    ]

    for w in workers:
        w.start()

    for i in range(5):
        q.put(f'задача {i}')

    for _ in workers:
        q.put(None)

    q.join()
    print('Все задачи выполнены')"""
        

def worker(task_q, result_q):
    while True:
        task = task_q.get()
        try:
            if task is None:
                break
            time.sleep(1)
            result = f'{task} - выполнено'
            result_q.put(result)
        finally:
            task_q.task_done()
"""      
if __name__ == '__main__':
    task_q = JoinableQueue()
    result_q = Queue()

    workers = [
        Process(target=worker, args=(task_q, result_q))
        for _ in range(2)
    ]

    for w in workers:
        w.start()

    for i in range(5):
        task_q.put(f'задача {i}')

    for _ in workers:
        task_q.put(None)

    task_q.join()
    print('Все задачи выполнены')

    for _ in range(5):
        print(result_q.get())

    print('Все результаты получены')"""

"""
производитель, кладет в JoinableQueue список чисел
потребитель, берет из JoinableQueue список чисел, квадрат, выводит результат
после обработки каждой задачи потребитель вызывает task_done()
join()
"""

def producer5(queue, numbers):
    for number in numbers:
        print(f"добавлен элемент {number}")
        queue.put(number)
        time.sleep(0.5)

    queue.put(None)
    print("производитель завершил работу")

def consumer5(queue):
    while True:
        item = queue.get()
        if item is None:
            queue.task_done()
            break
        print(f"получен элемент {item}, квадрат: {item ** 2}")
        time.sleep(0.5)
        queue.task_done()
    print("потребитель завершил работу")

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    queue = JoinableQueue()

    producer = Process(target=producer5, args=(queue, numbers))
    consumer = Process(target=consumer5, args=(queue,))

    producer.start()
    consumer.start()

    queue.join()
    producer.join()
    consumer.join()

    print("Все задачи выполнены")

from multiprocessing import Pool

"""with Pool(processes=4) as pool:
    ...
"""
"""
map(func, iterable) - многопроцессная версия map
starmap - аналогично map, но с возможностью передачи нескольких аргументов в функцию
apply(func, args) - Вызывает func(*args). Блокирует выполнение до завершения работы процесса. 
apply_async(func, args) - Вызывает func(*args) асинхронно, не блокируя выполнение. AsyncResult - объект, который содержит результат работы функции
imap(func, iterable) - аналогичен map(), но возвращает результаты по мере их готовности. Возвращает итератор
close() - закрывает доступ к очереди для добавления новых элементов
join() - ждет завершения всех процессов в пуле
"""

def square(x):
    return x * x

"""if __name__ == '__main__':
    with Pool(processes=4) as pool:
        results = pool.map(square, range(1, 11))
    print(results)"""
        
def slow_square(x):
    time.sleep(1)
    return x * x

"""if __name__ == '__main__':
    with Pool(2) as pool:
        results = pool.apply_async(slow_square, args=(5,))
        print('задача запущена')
        print('Результат:', results.get())"""

def fail(x):
    raise ValueError('Что-то пошло не так')

"""if __name__ == '__main__':
    with Pool(processes=1) as pool:
        res = pool.apply_async(fail, args=(10,))
        try:
            res.get()
        except Exception as e:
            print(e)"""

def power(x):
    return x ** 3

def callback(result):
    print(f"результат: {result}")

"""if __name__ == '__main__':
    with Pool(processes=2) as pool:
        for i in range(5):
            pool.apply_async(power, args=(i,), callback=callback)
        pool.close()
        pool.join()"""


# параллельная обработка с map
#from multiprocessing import Pool
#import time

def square(x):
    time.sleep(1)
    return x ** 2

"""if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]

    with Pool(2) as pool:
        results = pool.map(square, numbers)

    print(results)
"""

# параллельная обаботка starmap - аналогично map, но с возможностью передачи нескольких аргументов в функцию

def power(base, exponent):
    return base ** exponent

"""if __name__ == '__main__':
    data = [(2, 3), (3, 2), (4, 2), (5, 3)]

    with Pool(processes=2) as pool:
        results = pool.starmap(power, data)

    print(results)
"""

# apply / apply_async

def double(n):
    time.sleep(1)
    return n * 2

"""if __name__ == '__main__':
    with Pool(processes=2) as pool:
        result_sync = pool.apply(double, args=(5,))
        print("Результат синхронного вызова:", result_sync)

        async_result = pool.apply_async(double, args=(10,))
        print("Асинхронный вызов запущен")
        result_async = async_result.get()
        print("Результат асинхронного вызова:", result_async)"""

# callback

def multiply(n):
    time.sleep(1)
    return n * 3

def on_done(result):
    print("Результат получен через колбэк:", result)

"""if __name__ == '__main__':
    with Pool(processes=2) as pool:
        pool.apply_async(multiply, args=(5,), callback=on_done)
        
        print("основной процесс продолжает работу...")
        time.sleep(2)  """    

# error_calback

def unsafe_divide(x):
    if x == 0:
        raise ValueError("Деление на ноль!")
    return 10 / x

def on_result(result):
    print("Результат:", result)

def on_error(error):
    print("Ошибка:", error)

"""if __name__ == '__main__':
    with Pool(processes=2) as pool:
        pool.apply_async(unsafe_divide, args=(2,), callback=on_result, error_callback=on_error)
        pool.apply_async(unsafe_divide, args=(0,), callback=on_result, error_callback=on_error)
        
        pool.close()
        pool.join()
"""

"""
берёт список чисел [5, 7, -3, 8, 10]
запускает пул процессов для вычисления факториала каждого числа
если число отрицательное - выбрасывается исключение
результаты успешных вычислений собираются в список через callback
ошибки обрабатываются отдельно через error_callback
"""
"""

Value, Array
shared_memory
"""

def worker(data):
    data[0] = 999 # копия

"""if __name__ == '__main__':
    numbers = [1, 2, 3]
    p = Process(target=worker, args=(numbers,))
    p.start()
    p.join()
    print(numbers)"""


# Value для одной переменной
"""
i = integer
d = double/float
c = char
"""
from multiprocessing import Value

v = Value('i', 0)

def increment(v):
    for _ in range(5):
        time.sleep(0.1)
        v.value += 1


"""if __name__ == '__main__':
    val = Value('i', 0)
    p1 = Process(target=increment, args=(val,))
    p2 = Process(target=increment, args=(val,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Значение:", val.value)"""

# Array для массива
from multiprocessing import Array

a = Array('i', [1, 2, 3])

def double(arr):
    for i in range(len(arr)):
        arr[i] *= 2


"""if __name__ == '__main__':
    shared_array = Array('i', [1, 2, 3, 4])
    p = Process(target=double, args=(shared_array,))
    p.start()
    p.join()
    print("Результат:", list(shared_array))"""

# Lock - 
"""
lock.acquire() - захватить замок, если он свободен, иначе ожидать его освобождения.
lock.release() - освободить замок
with lock: - контекстный менеджер для безопасного доступа к защищенному ресурсу.
    # Критическая секция

lock.acquire()
try:
    # Критическая секция
    pass
finally:
    lock.release()
"""
# RLock -
val = Value('i', 0, lock=False) # небезопасно

from multiprocessing import Lock

lock = Lock()
val = Value('i', 0, lock=lock)

def safe_increment(v):
    with v.get_lock():
        v.value += 1

def increment(shared_val, lock):
    for _ in range(1000):
        with lock:
            shared_val.value += 1

"""if __name__ == '__main__':
    val = Value('i', 0)
    lock = Lock()

    p1 = Process(target=increment, args=(val, lock))
    p2 = Process(target=increment, args=(val, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Значение:", val.value)"""


def square_elements(arr, lock):
    with lock:
        for i in range(len(arr)):
            arr[i] *= arr[i]

"""if __name__ == '__main__':
    data = Array('i', [1, 2, 3, 4])
    lock = Lock()

    p1 = Process(target=square_elements, args=(data, lock))
    p2 = Process(target=square_elements, args=(data, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Результат:", list(data))"""

# подсчет общего количества операций
def increment(counter, lock):
    for _ in range(1000):
        with lock:
            counter.value += 1

"""if __name__ == '__main__':
    counter = Value('i', 0)
    lock = Lock()

    p1 = Process(target=increment, args=(counter, lock))
    p2 = Process(target=increment, args=(counter, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Общее количество операций:", counter.value)"""

# параллельная обработка списка

def square_elements(arr, start, end):
    for i in range(start, end):
        arr[i] = arr[i] ** 2

"""if __name__ == '__main__':
    arr = Array('i', [1, 2, 3, 4, 5])

    p1 = Process(target=square_elements, args=(arr, 0, 3))
    p2 = Process(target=square_elements, args=(arr, 3, 5))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Результат:", list(arr))"""


# гонка

def unsafe_increment(counter):
    for _ in range(1000):
        counter.value += 1

"""if __name__ == '__main__':
    counter = Value('i', 0)

    p1 = Process(target=unsafe_increment, args=(counter,))
    p2 = Process(target=unsafe_increment, args=(counter,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Значение:", counter.value)"""

# одновременное чтение и запись в массив
def writer(arr, lock):
    for i in range(len(arr)):
        with lock:
            arr[i] += 1
            time.sleep(0.1)

def reader(arr, lock):
    for _ in range(5):
        with lock:
            print("Чтение:", list(arr))
        time.sleep(0.15)

"""if __name__ == '__main__':
    arr = Array('i', [0, 0, 0, 0, 0])
    lock = Lock()

    p1 = Process(target=writer, args=(arr, lock))
    p2 = Process(target=reader, args=(arr, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Результат:", list(arr))"""

# параллельное суммирование массива

def partial_sum(arr, start, end, result, lock):
    local_sum = sum(arr[start:end])
    with lock:
        result.value += local_sum

"""if __name__ == '__main__':
    arr = Array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    result = Value('i', 0)
    lock = Lock()

    p1 = Process(target=partial_sum, args=(arr, 0, 5, result, lock))
    p2 = Process(target=partial_sum, args=(arr, 5, 10, result, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Сумма:", result.value)"""

"""
параллельная обработка массива с сохранением статистики
массив из 10 чисел
    1процесс: увеличивает каждый четный элемент на 10
    2процесс: увеличивает каждый нечетный элемент на 20

подсчитать общее количество операций, выполненных процессами
lock
"""

def increase_even(arr, lock, counter):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            with lock:
                arr[i] += 10
                counter.value += 1

def increase_odd(arr, lock, counter):
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            with lock:
                arr[i] += 20
                counter.value += 1

"""if __name__ == '__main__':
    arr = Array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    counter = Value('i', 0)
    lock = Lock()

    p1 = Process(target=increase_even, args=(arr, lock, counter))
    p2 = Process(target=increase_odd, args=(arr, lock, counter))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Результат:", list(arr))
    print("Общее количество операций:", counter.value)"""

"""
Manager - серверный процесс для доступа к обычным структурам
manager.list() - общий список
manager.dict() - общий словарь
manager.Queue() - общая очередь
manager.Value() 
manager.Namespace() - для произвольных атрибутов
"""

from multiprocessing import Manager

def worker(shared_list, name):
    shared_list.append(f"привет от {name}")

"""if __name__ == '__main__':
    manager = Manager()
    result_list = manager.list()

    processes = [
        Process(target=worker, args=(result_list, f"процесс {i}"))
        for i in range(5)
    ]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print("Результат:", list(result_list))"""

def add_data(shared_dict, key, value):
    shared_dict[key] = value

"""if __name__ == '__main__':
    manager = Manager()
    data_dict = manager.dict()

    processes = [
        Process(target=add_data, args=(data_dict, f"ключ_{i}", i*10))
        for i in range(4)
    ]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print("Результат:", dict(data_dict))"""


def worker(ns):
    ns.value += 1

"""if __name__ == '__main__':
    manager = Manager()
    ns = manager.Namespace()
    ns.value = 0

    processes = [Process(target=worker, args=(ns,)) for _ in range(5)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print("Результат:", ns.value)"""

"""
работа с общими объектами с помощью Manager
list
dict
Namespace

1
запустите 5 процессов. Каждый из них должен добавить в общий список строку
Привет от процесса N, где N - номер процесса
После завершения всех процессов выведите содержимое списка

2
создайте 3 процесса. Каждый из них должен добавить в общий словарь ключ-значение
ключ = имя процесса, значение = квадрат числа i, где i - [1, 2, 3]

3
смоделировать общий счетчик в Namespace. Запустить 5 процессов, каждый из которых увеличивает счетчик на 1. 
Вывести результат.

4
5 процессов, каждый
    добавить свое имя в общий список
    добавить в словарь ключ = имя процесса, значение = длина имени
"""

def add_message(shared_list, num):
    shared_list.append(f"Привет от процесса {num}")

"""if __name__ == '__main__':
    manager = Manager()
    messages = manager.list()

    processes = [Process(target=add_message, args=(messages, i)) for i in range(5)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print("Список сообщений:", list(messages))"""

def write_to_dict(shared_dict, name, value):
    shared_dict[name] = value

"""if __name__ == '__main__':
    manager = Manager()
    data = manager.dict()

    processes = []

    for i in range(1, 4):
        p = Process(target=write_to_dict, args=(data, f"proc-{i}", i**2))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Словарь:", dict(data))"""

def inrement_counter(ns):
    temp = ns.counter
    time.sleep(0.1)
    ns.counter = temp + 1

"""if __name__ == '__main__':
    manager = Manager()
    ns = manager.Namespace()
    ns.counter = 0

    processes = [Process(target=inrement_counter, args=(ns,)) for _ in range(5)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print("Результат:", ns.counter)"""

def update_all(shared_list, shared_dict, name):
    shared_list.append(name)
    shared_dict[name] = len(name)

# if __name__ == '__main__':
#     manager = Manager()
#     shared_list = manager.list()
#     shared_dict = manager.dict()

#     process_names = [f'процесс_{i}' for i in range(5)]
#     processes = [
#         Process(target=update_all, args=(shared_list, shared_dict, name))
#         for name in process_names
#     ]

#     for p in processes:
#         p.start()

#     for p in processes:
#         p.join()

#     print("Список имен:", list(shared_list))
#     print("Словарь:", dict(shared_dict))
    