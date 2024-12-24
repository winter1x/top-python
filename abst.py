from abc import ABC, abstractmethod
#создать абстрактный MClass с несколькими абстрактными методами\
# в другом файле импортировать его и реализовать в наследнике
class Animal(ABC):
    info = 'animal'
    @abstractmethod
    def make_voice(self):
        pass

    @abstractmethod
    def walk(self):
        pass

