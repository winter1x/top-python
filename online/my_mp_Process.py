"""
GIL

Process - отдельный процесс
Queue - очередь
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
if __name__ == '__main__':
    # p = Process(target=print_square, args=(2,)
    # p = Process(target=show_info, name='процесс-1')
    # p = MyProcess("текст")
    # p.start()
    # p.join()
    print('-' * 40)
    processes = []
    for i in range(5):
        p = Process(target=worker, args=(i,))
        processes.append(p)
        p.start()
        print(p.name, p.is_alive())
    print('-' * 40)
    time.sleep(1)
    for p in processes:
        print(p.name, p.is_alive())
        if p.is_alive():
            p.terminate()
            print("процесс {0} остановлен".format(p.name))
            
    for p in processes:
        p.join()
        print("процесс {0} завершен".format(p.name))

    
"""
запуск 5 процессов, работа через sleep
логирование

каждый процесс получает разное/случайное [1-5]c. время работы
использовать args
использовать join
"""