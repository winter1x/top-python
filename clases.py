class Person:

    health = 100

    def __init__(self, name, age, is_student=False):
        self.name = name
        self.age = age
        self.is_student = is_student
        self.gender = None

    def invert_is_student(self):
        self.is_student = not self.is_student

    @staticmethod
    def to_learn():
        print('im learning')

    @classmethod
    def print_health(cls):
        print(cls.health)

Matvey = Person('name', 18)
print(Matvey.is_student)
Matvey.invert_is_student()
print(Matvey.is_student)
Matvey.to_learn()
Person.print_health()

# создать математический класс с атрибутом количества
# несколько методов cls которые возвращают генератор
# init принимает список строк с желаемыми функциями
# метод который их выводит

class MClass:
    length = 5

    def __init__(self, func):
        self.func = func

    def print_func(self):
        print(self.func)

    @classmethod
    def gen1(cls):
        return [i for i in range(cls.length)]

    @classmethod
    def gen2(cls):
        return [i**2 for i in range(cls.length)]

print(MClass.length)
print(MClass.gen1())
print(MClass.gen2())
MyMath = MClass(['sum', 'pow'])
MyMath.print_func()
