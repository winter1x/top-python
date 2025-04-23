"""
метакласс PrintMeta
каждый раз при создании нового класса выводит
Класс <ИмяКласса> создан.
"""
class PrintMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Класс {name} создан.")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=PrintMeta):
    pass
"""
метакласс UpperAttrMeta
преобразует все имена атрибутов в верхний регистр
"""
class UpperAttrMeta(type):
    def __new__(cls, name, bases, dct):
        new_dct = {}
        for key, value in dct.items():
            if not key.startswith("__") and not callable(value):
                new_dct[key.upper()] = value
            else:
                new_dct[key] = value
        return super().__new__(cls, name, bases, new_dct)

class MyClass(metaclass=UpperAttrMeta):
    foo = 1
    bar = 2

print(hasattr(MyClass, 'foo'))
print(MyClass.FOO)
"""
метакласс ValidatedModel
проверяет чтобы каждый класс созданный с его помощью обязательно имел атрибут fields и был списком
TypeError
"""
class ValidatedModel(type):
    def __new__(cls, name, bases, dct):
        if 'fields' not in dct:
            raise TypeError("")
        if not isinstance(dct['fields'], list):
            raise TypeError("")
        return super().__new__(cls, name, bases, dct)

class User(metaclass=ValidatedModel):
    fields = ['name', 'email']

"""
class Broken(metaclass=ValidatedModel):
    pass
"""
"""
метакласс RegistryMeta
автоматически регистрирует все создаваемые с его помощью классы в переменной
"""
CLASS_REGISTRY = {}
class RegistryMeta(type):
    def __init__(cls, name, bases, dct):
        CLASS_REGISTRY[name] = cls
        super().__init__(name, bases, dct)

class BaseModel(metaclass=RegistryMeta):
    pass

class Proguct(metaclass=RegistryMeta):
    pass

class Customer(metaclass=RegistryMeta):
    pass

"""
чтобы имя каждого создаваемого класса начиналось с большой буквы"""

class CapitalizedMeta(type):
    def __new__(cls, name, bases, dct):
        if not name[0].isupper():
            raise TypeError("")
        return super().__new__(cls, name, bases, dct)

class ProperName(metaclass=CapitalizedMeta):
    pass

"""class badName(metaclass=CapitalizedMeta):
    pass"""