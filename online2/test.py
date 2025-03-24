# с помощью timeit замерить выполнение fibonacci с cache и без cache
import timeit

def fibonnaci_no_cache(n):
    if n <= 1:
        return n
    return fibonnaci_no_cache(n - 1) + fibonnaci_no_cache(n - 2)

time = timeit.timeit(lambda: fibonnaci_no_cache(30), number=2)
print(time)


from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_with_cache(n):
    if n <= 1:
        return n
    return fibonacci_with_cache(n - 1) + fibonacci_with_cache(n - 2)

time2 = timeit.timeit(lambda: fibonacci_with_cache(30), number=2)
print(time2)
print(time2 / time)
