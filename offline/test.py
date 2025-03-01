class UltraComplexMathOperations:
    def __init__(self):
        pass

    def execute(self, num1, num2, operation_type):
        if operation_type == "addition":
            result = self.__very_complicated_addition(num1, num2)
        elif operation_type == "subtraction":
            result = self.__very_complicated_subtraction(num1, num2)
        elif operation_type == "multiplication":
            result = self.__very_complicated_multiplication(num1, num2)
        elif operation_type == "division":
            if num2 != 0:
                result = self.__very_complicated_division(num1, num2)
            else:
                return "Error: Division by zero!"
        else:
            return "Unknown operation"
        return f"Result: {result}"

    def __very_complicated_addition(self, a, b):
        sum_value = 0
        for _ in range(abs(a)):
            sum_value += 1 if a > 0 else -1
        for _ in range(abs(b)):
            sum_value += 1 if b > 0 else -1
        return sum_value

    def __very_complicated_subtraction(self, a, b):
        sum_value = self.__very_complicated_addition(a, -b)
        return sum_value

    def __very_complicated_multiplication(self, a, b):
        product = 0
        for _ in range(abs(b)):
            product = self.__very_complicated_addition(product, a)
        return product if b >= 0 else -product

    def __very_complicated_division(self, a, b):
        count = 0
        temp_a = abs(a)
        while temp_a >= abs(b):
            temp_a = self.__very_complicated_subtraction(temp_a, abs(b))
            count = self.__very_complicated_addition(count, 1)
        return count if (a >= 0 and b > 0) or (a < 0 and b < 0) else -count


# Использование
math_op = UltraComplexMathOperations()
print(math_op.execute(10, 2, "addition"))
print(math_op.execute(10, 2, "subtraction"))
print(math_op.execute(10, 2, "multiplication"))
print(math_op.execute(10, 2, "division"))
