"""
threading
для чего нужны:
параллелизм
реактивность
эффектовное исполнение ожиданий 
маштабирование на многопроцессорных системах
I/O-bound задач

GIL

неэффективны:
многочисленные вычисления на CPU (тут нужен multiprocessing)

race condition условная гонка/состояние гонки
deadlock взаимные блокировки
starvation голодание
трудность отладки

синхронизация потоков:
Lock - примитив синхронизации для управления доступом к общим ресурсам
Rlock, Semaphore, Condition, Event - для координации работы потоков
queue.Queue - потокобезная очередь для обмена данными между потоками
    put(item, block=True, timeout=None) - добавить элемент в очередь
    get(block=True, timeout=None) - получить элемент из очереди
    task_done() - сообщает очереди, что текущая задача выполнена
    join() - ожидание завершения всех потоков
    empty(), full(), qsize() - информация об очереди. Небезопасны

Thread - класс, реализующий поток исполнения кода
    передать целевую функцию через параметр target=
    создать свой класс на основе класса Thread и переопределить метод .run()

    .start() запуск потока
    .run() метод исполнения
    .join(timeout=None) - ожидание завершения потока, если не передан таймаут, то будет ждать пока не завершится поток
    .is_alive() - проверка на активность потока
    .name, .ident - имя и идентификатор потока

    жизненный цикл потока:
        Создан = Thread
        Запущен = start()
        Работает = .run()
        Завершен 

ThreadPool
Barrier

Lock
    lock.acquire(blocking=True, timeout=-1) - захватить блокировку, если она свободна
    lock.release() - освободить блокировку
with lock:
    # код, который нужно защитить

RLock - рекурсивный замок

Semaphore(value) - для нескольких потоков можно использовать семафоры, 
    которые ограничивают количество одновременно выполняющихся потоков

    acquire(blocking=True, timeout=None) - попытка захватить семафор, уменьшая счетчик внутреннего состояния
    release() - освобождение семафора, увеличивая счетчик

    with semaphore:

BoundedSemaphore() - счетчик должен быть больше нуля

Event - сигнализация между потоками
    .wait() - ожидание сигнала. Блокируется поток до тех пор, пока сигнал не будет установлен
    .set() - установка сигнала. Разблокирует все ожидающие потоки
    .clear() - сброс сигнала. Потоки снова будут заблокированы
    .is_set() - проверка состояния сигнала

Condition - расширенный механизм ожидания
    wait() - ожидание сигнала. Блокируется поток до тех пор, пока сигнал не будет установлен
    notify() / notify_all() - уведомление ожидающих потоков

Timer - запуск потока через заданный интервал времени

threading.current_thread() - возвращает текущий поток (объект)
threading.enumerate() - список всех активных потоков
threading.active_count() - количество активных потоков
"""
from threading import Thread, current_thread

def worker():
    print('работает поток', current_thread().name)

t = Thread(target=worker)
t.start()

class MyThread(Thread):
    def run(self):
        print("Работает поток через наследование")

t = MyThread()
t.start()

t = Thread(target=lambda: print('просто функция'))
t.start()
t.join()
print("все потоки завершили работу")


def greet(name, greeting='hello'):
    print(f'{greeting}, {name}')

t = Thread(target=greet, args=('Alice', ), kwargs={'greeting': 'Hi'})
t.start()

import time

def slow_task(name):
    print(f'Начал выполнение задачи {name}')
    time.sleep(0.1)
    print(f'Завершил выполнение задачи {name}')

threads = []
for i in range(3):
    t = Thread(target=slow_task, args=(f'task-{i}', ))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print('Все потоки завершили работу')

from threading import Lock

counter = 0
lock = Lock()

def increment():
    global counter
    for _ in range(1000000):
        with lock:
            global counter
            counter += 1

threads = [Thread(target=increment) for _ in range(2)]

[t.start() for t in threads]
[t.join() for t in threads]

print(f'counter = {counter}')

"""if lock.acquire(timeout=1.5):
    try:
        # критическая секция
    finally:
        lock.release()
else:
    print('не удалось захватить ресурс')"""

from threading import RLock
lock = RLock()

def recursive(n):
    if n <= 0:
        return

    with lock:
        print(f'захват на глубине {n}')
        recursive(n - 1)

recursive(3)

lock1 = Lock()
lock2 = Lock()

"""
deadlock
def thread1():
    with lock1:
        print('захват lock1')
        time.sleep(1)
        print('пытаемся захватить lock2')
        with lock2:
            print('захватил lock2')

def thread2():
    with lock2:
        print('захват lock2')
        time.sleep(1)
        print('пытаемся захватить lock1')
        with lock1:
            print('захватил lock1')

t = Thread(target=thread1)
t.start()

t2 = Thread(target=thread2)
t2.start()"""

from threading import Semaphore
sema = Semaphore(2)

def worker(num):
    print(f"поток {num} ждет доступ ")
    with sema:
        print(f"поток {num} получил доступ")
        time.sleep(2)
        print(f"поток {num} освободил доступ")

threads = [Thread(target=worker, args=(i, )) for i in range(5)]

[t.start() for t in threads]
[t.join() for t in threads]

from threading import BoundedSemaphore
"""
sema = BoundedSemaphore(2)
sema.acquire()
sema.release()
sema.release()"""

import random

download_sema = Semaphore(3)

def download_file(file_id):
    print(f"Файл {file_id}: ожидание слота")
    with download_sema:
        print(f"Файл {file_id}: скачивается")
        time.sleep(random.randint(1, 3))
        print(f"Файл {file_id}: скачался")

threads = [Thread(target=download_file, args=(i, )) for i in range(10)]

[t.start() for t in threads]
[t.join() for t in threads]

"""
1 параллельная печать с блокировкой
5 потоков, печатают от 1 до 3. Поток в критичческой секции, защищен Lock
"""
lock = Lock()
def print_numbers(name):
    for i in range(1, 4):
        with lock:
            print(f"поток {name}: {i}")
        time.sleep(0.2)

threads = []

for i in range(5):
    t = Thread(target=print_numbers, args=(f"поток-{i}", ))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

"""
2 рекурсивная блокировка
поток, вызывает функцию внутри функции (рекурсивный вызов). обе используют одну и ту же блокировку
"""
rlock = RLock()

def inner():
    with rlock:
        print('внутренняя функция')

def outer():
    with rlock:
        print('внешняя функция')
        inner()

t = Thread(target=outer)
t.start()
t.join()
"""
3 ограничение количества одновременных подключений
запустите 10 потоков, работают по 2 секу. Не более 3 потоков одновременно
"""
sem = Semaphore(3)
def worker(n):
    with sem:
        print(f"поток {n} захватил ресурс")
        time.sleep(2)
        print(f"поток {n} освободил ресурс")

threads = []
for i in range(10):
    t = Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

[t.join() for t in threads]

"""
4 контроль использования ресурса
создать BoundedSemaphore(2), попробовать вызвать release() больше чем acquire() раз. Обработка ошибок
"""
sem = BoundedSemaphore(2)

sem.acquire()
sem.acquire()
try:
    sem.release()
    sem.release()
    sem.release()
except ValueError as e:
    print(f'ошибка {e}')

"""
5 сравнение Lock и Semaphore
сделать принтер. использовать с lock, semaphore3
"""
printer_lock = Lock()
printer_sem = Semaphore(3)

def lock_user(n):
    with printer_lock:
        print(f"[Lock] Поток {n} использует принтер")
        time.sleep(1)

def sem_user(n):
    with printer_sem:
        print(f"[Semaphore] Поток {n} использует принтер")
        time.sleep(1)

print('Запуск потоков с Lock')
threads = [Thread(target=lock_user, args=(i, )) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()

print('Запуск потоков с Semaphore')
threads = [Thread(target=sem_user, args=(i, )) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()

from threading import Condition

condition = Condition

with condition:
    condition.wait()

with condition:
    condition.notify()
    
#while not <condition>: condition.wait()

from threading import Event
event = Event()
event.set()
event.clear()
if event.is_set():
    print("можно продолжить")
event.wait(timeout=None)


event = Event()

def worker():
    print("поток ожидает события")
    event.wait()
    print("поток получил событие")

t = Thread(target=worker)
t.start

time.sleep(2)
print("посылаю сигнал")
event.set()

t.join()


event = Event()

def ready_worker(i):
    print(f"поток {i} ждет запуска")
    event.wait()
    print(f"поток {i} стартует")

threads = [Thread(target=ready_worker, args=(i, )) for i in range(5)]
for t in threads: t.start()

time.sleep(2)
print("стартуем все потоки")
event.set()

from queue import Queue
q = Queue()
q = Queue(maxsize=10) # ограничение на кол-во элементов в очереди


def producer(q):
    for i in range(5):
        print("производитель отправляет данные")
        q.put(i)
        time.sleep(1)

def consumer(q):
    while True:
        item = q.get()
        print(f"получено: {item}")
        q.task_done()

q = Queue()
t1 = Thread(target=producer, args=(q,))
t2 = Thread(target=consumer, args=(q,))
t1.start()
t2.start()
t1.join()
q.join()
