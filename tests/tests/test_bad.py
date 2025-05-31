"""user = {}

def test_first():
    user['first'] = 'john'


def test_last():
    assert user['last'] == 'smith'
"""

"""def test_something():
    if (something):
        # 1 способ
        # проверка
    else:
        # 2 способ
        # проверка
    # проверка
"""

import pytest

@pytest.fixture
def result():
    return sum([5, 9])

def test_sum(result):
    assert result == 14

def test_create_user():
    user = {'name': 'John', 'age': 30}
    assert user['age'] == 30

def test_create_user2():
    user = {'name': 'John', 'age': 30}
    assert user['name'] == 'John'