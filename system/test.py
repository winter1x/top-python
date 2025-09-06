from threading import Lock, Thread
import time
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