from dataclasses import dataclass
from math import gcd


@dataclass
class  Fraction:
    numerator: int
    denominator: int

    def __post_init__(self):
        if self.denominator == 0:
            raise ZeroDivisionError("")
        self._reduce()

    def _reduce(self):
        """сокращает дробь"""
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator


    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator

            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator

            return Fraction(new_numerator, new_denominator)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ZeroDivisionError("")
            return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        return NotImplemented


frac1 = Fraction(1, 2)
frac2 = Fraction(3, 4)
print(frac1 * frac2)
print(frac1 / frac2)
print(frac1 - frac2)
print(frac1 + frac2)