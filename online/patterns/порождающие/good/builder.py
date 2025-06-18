"""
собирает продукт шаг за шагом

структура:
Builder строитель - определяет интерфейс для пошагового построения 
ConcreteBuilder конкретный строитель - реализует интерфейс строителя и собирает конечный объект
Product продукт - создаваемый объект
Director директор - координирует шаги построения объекта с помощью конкретного строителя
Client клиент - запускает процеес (директора/билдер) 

(+)
гибкость
пошаговая сборка
изоляция кода построения 
повторное использование

(-)
много классов
сложнее __init__()
дополнительная абстракция

применяем когда:
создание объектов требует много шагов
много опциональных параметров
разные вариации создаваемых объектов
разделить создание и использование объекта

Factory Method создает один объект, а Builder собирает его пошагово
Abstract Factory создает семейство объектов, а Builder собирает один объект
Prototype клонирует объекты, а Builder создает их с нуля

плохой телескопический вариант Car(color=red, engine=1.6, wheels=4, has_spoiler=True, ...)

решение
builder = SportsCarBuilder()
builder.set_color(color='red')]
builder.set_engine(engine=1.6)
builder.set_wheels(wheels=4)
car = builder.build()
"""
"""
создаем сложные объекты пошагово, когда есть параметры/несколько этапов
"""

"""
builder 
интерфейс строителя 
абстрактный интерфейс

concrete builders
конкретные строители 
реализуют builder

product
наш сложный объект

director
управление, порядок вызова методов строителя, строителей
"""
from abc import ABC, abstractmethod

#интерфейс строителя
class Builder(ABC):
    @abstractmethod
    def build_part_a(self):
        pass

    @abstractmethod
    def build_part_b(self):
        pass

    @abstractmethod
    def get_product(self):
        pass

#конкретный строитель
class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.part_a = "Part A"

    def build_part_b(self):
        self.product.part_a = "Part B"

    def get_product(self):
        return self.product

#продукт
class Product:
    def __init__(self):
        self.part_a = None
        self.part_b = None

    def __str__(self):
        return f"Product: part_a={self.part_a}, part_b={self.part_b}"

#директор
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_part_a()
        self.builder.build_part_b()
        return self.builder.get_product()

if __name__ == "__main__":
    builder = ConcreteBuilder()
    director = Director(builder)
    product = director.construct()
    print(product)


print('#------------------------------------------------------------------------------')

class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None

    def __str__(self):
        return f"Computer: CPU={self.cpu}, RAM={self.ram}, Storage={self.storage}, GPU={self.gpu}"

from abc import ABC, abstractmethod

class ComputerBuilder(ABC):
    def __init__(self):
        self.computer = Computer()

    @abstractmethod
    def set_cpu(self): pass

    @abstractmethod
    def set_ram(self): pass

    @abstractmethod
    def set_storage(self): pass

    @abstractmethod
    def set_gpu(self): pass

    def get_result(self):
        return self.computer

class GamingComputerBuilder(ComputerBuilder):
    def set_cpu(self): self.computer.cpu = "Intel i7"
    def set_ram(self): self.computer.ram = "16GB"
    def set_storage(self): self.computer.storage = "1TB SSD"
    def set_gpu(self): self.computer.gpu = "NVIDIA GeForce RTX 3080"

class OfficeComputerBuilder(ComputerBuilder):
    def set_cpu(self): self.computer.cpu = "Intel i5"
    def set_ram(self): self.computer.ram = "8GB"
    def set_storage(self): self.computer.storage = "500GB HDD"
    def set_gpu(self): self.computer.gpu = "Intel HD Graphics"

class ComputerDirector:
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder

    def build_computer(self):
        self.builder.set_cpu()
        self.builder.set_ram()
        self.builder.set_storage()
        self.builder.set_gpu()
        
builder = GamingComputerBuilder()
director = ComputerDirector(builder)
director.build_computer()
gaminc_pc = builder.get_result()
print(gaminc_pc)

builder = OfficeComputerBuilder()
director = ComputerDirector(builder)
director.build_computer()
office_pc = builder.get_result()
print(office_pc)


"""
Builder
создание туристических туров
набор компонентов тура:
проживание
экскурсии
транспорт
питание
страховка

Tour объект сборки
TourBuilder интерфейс сборки
    add_acommodation()
    add_excursions()
    add_transport()
    add_meals()
    add_insurance()
    get_result()

StandardTourBuilder конкретный билдер собирает обект Tour
TourDirector задает порядок шагов билдера
"""

class Tour:
    def __init__(self):
        self.parts = []

    def add(self, part: str):
        self.parts.append(part)

    def __str__(self):
        print("Tour parts:", ', '.join(self.parts))

#from abc import ABC, abstractmethod

class TourBuilder(ABC):
    @abstractmethod
    def add_acommodation(self): pass

    @abstractmethod
    def add_excursions(self): pass

    @abstractmethod
    def add_transport(self): pass

    @abstractmethod
    def add_meals(self): pass

    @abstractmethod
    def add_insurance(self): pass

    @abstractmethod
    def get_result(self) -> Tour: pass

class StandardTourBuilder(TourBuilder):
    def __init__(self):
        self.tour = Tour()

    def add_acommodation(self): self.tour.add('accommodation')

    def add_excursions(self): self.tour.add('excursions')

    def add_transport(self): self.tour.add('transport')

    def add_meals(self): self.tour.add('meals')

    def add_insurance(self): self.tour.add('insurance')

    def get_result(self) -> Tour: return self.tour

class TourDirector:
    def __init__(self, builder: TourBuilder):
        self.builder = builder

    def build_minimal_tour(self):
        self.builder.add_acommodation()
        self.builder.add_excursions()

    def build_full_tour(self):
        self.builder.add_acommodation()
        self.builder.add_excursions()
        self.builder.add_transport()
        self.builder.add_meals()
        self.builder.add_insurance()

builder1 = StandardTourBuilder()
director1 = TourDirector(builder1)
director1.build_minimal_tour()
tour1 = builder1.get_result()
tour1.__str__()
print()

builder2 = StandardTourBuilder()
director2 = TourDirector(builder2)
director2.build_full_tour()
tour2 = builder2.get_result()
tour2.__str__()
print()
