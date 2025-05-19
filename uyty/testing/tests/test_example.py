from my_pytest.example import reverse


def test_reverse():
    assert reverse("Src") == "crS"


def test_reverse_for_empty_string():
    assert reverse("") == ""

def test_stack_is_empty():
    stack = []
    assert not stack

def test_stack_append():
    stack = []
    stack.append(1)
    assert bool(stack)

def test_stack_pop():
    stack = [1]
    stack.pop()
    assert not stack

import time
import pytest

@pytest.fixture
def now():
    return int(time.time() * 1000)

def test_first_example():
    print(now)

def test_second_example():
    print(now)