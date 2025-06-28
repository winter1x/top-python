from threading import Timer, Lock, Thread
import time
from concurrent.futures import ThreadPoolExecutor
import requests
from queue import Queue
from threading import Barrier
import random
from concurrent.futures import as_completed

def fetch(url):
    delay = random.uniform(0.5, 2.0)
    print(f"[Start] Загрузка {url} с задержкой {delay:.2f} секунд")
    time.sleep(delay)

    if random.random() < 0.2:
        raise Exception(f"Ошибка загрузки {url}")

    print(f"[End] Загрузка {url} завершена")
    return f"Результат загрузки {url}"

urls = [f"http://site{i}.com" for i in range(1, 11)]

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = {executor.submit(fetch, url): url for url in urls}

    for future in as_completed(futures):
        url = futures[future]
        try:
            result = future.result()
            print(f"Результат загрузки {url}: {result}")
        except Exception as exc:
            print(f"Ошибка загрузки {url}: {exc}")