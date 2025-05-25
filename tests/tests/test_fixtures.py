"""
pydash

includes()
size()
filter()
...(20)
"""
import time
from pydash import collections

coll = ['One', "true", 3, 10, 'cat', {}, '', 10, False]

def test_includes():
    assert collections.includes(coll, 3) == True
    assert collections.includes(coll, 'dog') == False

def test_size():
    assert collections.size(coll) == 9


now = int(time.time() * 1000)

def test_first_example():
    print(now)

def test_second_example():
    print(now)

