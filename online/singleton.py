class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        if not hasattr(self, "value"):
            self.value = value

obj1 = Singleton("первый")
obj2 = Singleton("второй")

print(obj1 is obj2) # True

print(obj1.value)
print(obj2.value)


def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return  get_instance

@singleton
class Singleton2:
    def __init__(self, value):
        self.value = value

obj3 = Singleton2("первый")
obj4 = Singleton2("второй")

print(obj3 is obj4)