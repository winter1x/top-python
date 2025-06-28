from threading import Timer, Lock, Thread
import time
from concurrent.futures import ThreadPoolExecutor
import requests
from queue import Queue
from threading import Barrier

barrier = Barrier(parties=3, timeout=3)

def worker(n):
    print(f"Поток {n} работа до барьера")
    time.sleep(n)
    print(f"Поток {n} подошел к барьеру")
    barrier.wait()
    print(f"Поток {n} продолжил выполнение")

threads = []

for i in range(3):
    t = Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()