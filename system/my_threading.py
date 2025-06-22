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
Queue - потокобезная очередь для обмена данными между потоками

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
Lock
    lock.acquire(blocking=True, timeout=-1) - захватить блокировку, если она свободна
    lock.release() - освободить блокировку
with lock:
    # код, который нужно защитить

RLock - рекурсивный замок
Semaphore(value) - для нескольких потоков можно использовать семафоры, 
    которые ограничивают количество одновременно выполняющихся потоков
Event - сигнализация между потоками
    .wait() - ожидание сигнала. Блокируется поток до тех пор, пока сигнал не будет установлен
    .set() - установка сигнала. Разблокирует все ожидающие потоки
    .clear() - сброс сигнала. Потоки снова будут заблокированы
Condition - расширенный механизм ожидания
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
t2.start()

