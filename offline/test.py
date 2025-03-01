from dataclasses import dataclass
from functools import total_ordering

@total_ordering
@dataclass
class Library:
    name: str
    address: str
    books_count: int

    def __add__(self, value: int):
        if not isinstance(value, int):
            raise ValueError("")
        return Library(self.name, self.address, self.books_count + value)

    def __iadd__(self, value: int):
        if not isinstance(value, int):
            raise ValueError("")
        self.books_count += value
        return self

    #-
    def __sub__(self, other):
        pass

    # -=
    def __isub__(self, other):
        pass

    def __eq__(self, other):
        if not isinstance(other, Library):
            raise NotImplemented("")
        return self.books_count == other.books_count

    #<
    def __lt__(self, other):
        pass

