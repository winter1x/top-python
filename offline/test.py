from abc import ABC, abstractmethod


# Интерфейс работника
class IWorker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass


# Обычный работник (человек)
class Worker(IWorker):
    def work(self):
        print("Рабочий работает")

    def eat(self):
        print("Рабочий обедает")


# Робот (не должен иметь метод eat)
class RobotWorker(IWorker):
    def work(self):
        print("Робот работает")

    def eat(self):
        raise NotImplementedError("Робот не ест!")
