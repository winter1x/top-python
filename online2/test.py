"""
В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, 
сколько раз оно встречалось в этом тексте ранее.

Словом считается последовательность не пробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.
"""

"""
получить текущее через datetime
измерить время выполнения 
вывести в удобном формате через time
рассчитать разницу между двумя датами через datetime
"""
from datetime import datetime, timedelta
now = datetime.now()
print(now)

import timeit
code1 = """
for i in range(100000):
    pass
"""
ex_time = timeit.timeit(code1, number=1)
print(ex_time)

import time
timestamp = time.time()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
print(formatted_time)

date1 = datetime(2025, 3, 17)
date2 = datetime(2025, 3, 24)

delta = date2 - date1
print(delta)