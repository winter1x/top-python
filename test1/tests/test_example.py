from my_pytest.example import reverse
import pytest

def test_reverse():
    assert reverse("Src") == "crS"


def test_reverse_for_empty_string():
    assert reverse("") == ""


def test_stack():
    stack = []
    stack.append(1)
    stack.append(2)

    assert stack.pop() == 2
    assert stack.pop() == 1


def test_pop_with_empty_stack():
    stack = []
    with pytest.raises(IndexError):
        stack.pop()