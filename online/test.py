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