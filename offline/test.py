from dataclasses import dataclass
from datetime import date, timedelta

@dataclass
class Date:
    day: int
    month: int
    year: int

    def to_date(self):
        return date(self.year, self.month, self.day)

    def __sub__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        return abs((self.to_date() - other.to_date()).days)

    def __add__(self, days):
        if not isinstance(days, int):
            raise ValueError("")
        new_date = self.to_date() + timedelta(days=days)
        return Date(new_date.day, new_date.month, new_date.year)

    def __repr__(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year}"
