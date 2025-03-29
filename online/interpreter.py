#interpreter
"""
разбираем и вычисляем выражения разного языка
"""
"""
причины использования

предметная область
простая ограниченная грамматика
легко добавлять новые операции
"""

"""
нет

очень сложный
большое количество правил
редко меняются
"""

"""
структура

expression
concrete expressions
context
"""

# 2 + 3 * 4

from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def interpret(self) -> int:
        pass

class Number(Expression):
    def __init__(self, value: int):
        self.value = value

    def interpret(self) -> int:
        return self.value

class Addition(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> int:
        return self.left.interpret() + self.right.interpret()

class Multiplication(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> int:
        return self.left.interpret() * self.right.interpret()

class Subtraction(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self) -> int:
        return self.left.interpret() - self.right.interpret()


expr = Addition(Number(2), Multiplication(Number(3), Number(4)))

result = expr.interpret()
print(result)

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y
}

def interpret(expression: str) -> int:
    tokens = expression.split()
    left, op, right = int(tokens[0]), tokens[1], int(tokens[2])
    return operations[op](left, right)

print(interpret("2 + 3"))