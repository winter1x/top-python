from threading import Timer, Lock, Thread
import time
from concurrent.futures import ThreadPoolExecutor
import requests
from queue import Queue
from threading import Barrier
import random
from concurrent.futures import as_completed

NUM_THREADS = 5

barrier = Barrier(NUM_THREADS)

def worker(thread_id):
    for phase in range(1, 4):
        time.sleep(random.uniform(0.5, 2.0))
        print(f"[Поток {thread_id}] завершил фазу {phase}, ждет")

        barrier.wait()

        if phase < 3:
            print(f"[Поток {thread_id}] переходит к фазе {phase + 1}")

threads = []
for i in range(NUM_THREADS):
    t = Thread(target=worker, args=(i + 1,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Все потоки завершили работу")