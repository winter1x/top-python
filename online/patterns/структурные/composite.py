"""
структура:
компонент
leaf
composite контейнер
client

+
прозрачность
расширяемость
рекурсивность

применяем когда
древовидная структура
однаковая обработка элементов
код должен одинаково работать с различными компонентами

decorator - добавление функционала
bridge - разделение абстракции и реализации
chain of responsibility обрабатывает по цепочке
"""

class FileSystemComponent:
    def display(self, indent=0):
        raise NotImplementedError

class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print(' ' * indent + f"File {self.name}")


class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children  = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def display(self, indent=0):
        print(' ' * indent + f"Folder {self.name}")
        for child in self.children:
            child.display(indent + 2)

root = Folder("root")
root.add(File("1.txt"))
root.add(File("2.txt"))

sub = Folder("src")
sub.add(File('3.txt'))
sub.add(File('4.txt'))

nested = Folder("tests")
nested.add(File("5.txt"))
nested.add(File("6.txt"))

sub.add(nested)
root.add(sub)

root.display()

"""
composite

MenuComponent
MenuItem
MenuGroup
render
"""

class MenuComponent:
    def render(self, indent=0):
        raise NotImplementedError

class MenuItem(MenuComponent):
    def __init__(self, title, link):
        self.title = title
        self.link = link

    def render(self, indent=0):
        print(' ' * indent + f'{self.title} ({self.link})')

class MenuGroup(MenuComponent):
    def __init__(self, title):
        self.title = title
        self.children = []

    def add(self, component: MenuComponent):
        self.children.append(component)

    def render(self, indent=0):
        print(' ' * indent + f'{self.title}')
        for child in self.children:
            child.render(indent + 1)

main_menu = MenuGroup("меню сайта")
main_menu.add(MenuItem("главная", '/'))
main_menu.add(MenuItem('о компании', "/about"))

services = MenuGroup("услуги")
services.add(MenuItem("разработка сайтов", "/services/web"))
services.add(MenuItem("мобильные приложения", "/services/mobile"))

main_menu.add(services)
main_menu.add(MenuItem("контакты", "/contacts"))

main_menu.render()

"""
вычислительная система
вложенные
(2+3)*(4-1)
число - лист
операция - компонент

class Expression def evaluate
классы-листья Number
классы-композиты
Addition, Subtraction, Multiplication, Division принимают два дочерних выражения, которые реализуют интерфейс Expression

""" 
expr = Multiplication(
    Addition(Number(2), Number(3)),
    Subtraction(Number(4), Number(1))
)
print(expr.evaluate()) #15