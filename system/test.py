from threading import Timer, Lock, Thread
import time
from concurrent.futures import ThreadPoolExecutor
import requests
from queue import Queue
from threading import Barrier

NUM_TASKS = 10
NUM_CONSUMERS = 3

task_queue = Queue()

def producer():
    for i in range(NUM_TASKS):
        task_name = f"task-{i}"
        print(f"[Producer] добавляем задачу {task_name}")
        task_queue.put(task_name)
        time.sleep(0.1)
    
    for _ in range(NUM_CONSUMERS):
        task_queue.put(None)

def consumer(thread_id):
    while True:
        task = task_queue.get()
        if task is None:
            print(f"[Consumer {thread_id}] получили сигнал о завершении")
            task_queue.task_done()
            break
        print(f"[Consumer {thread_id}] обработка задачи {task}")
        time.sleep(0.5)
        print(f"[Consumer {thread_id}] задача {task} завершена")
        task_queue.task_done()

producer_thread = Thread(target=producer)
producer_thread.start()

consumer_threads = []
for i in range(NUM_CONSUMERS):
    t = Thread(target=consumer, args=(i,))
    t.start()
    consumer_threads.append(t)

task_queue.join()
producer_thread.join()
for t in consumer_threads:
    t.join()

print("Все задачи обработаны")