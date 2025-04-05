"""
История команд

5 последних действий
несколько устройств (тв кондиционер)
комбинация команд (макрос) [f1, f2, f3]
вкл все
выкл все
"""
"""
command

история команд, чтобы можно было посмотреть последние 5 действий.
несколько устройств телевизор, кондиционер
комбинировация команд в макрос например, Включить всё  включает сразу несколько устройств
"""
from abc import ABC, abstractmethod
from collections import deque

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class Light:
    def turn_on(self):
        print("Свет включен")

    def turn_off(self):
        print("Свет выключен")

class TV:
    def turn_on(self):
        print("Телевизор включен")

    def turn_off(self):
        print("Телевизор выключен")

class AC:
    def turn_on(self):
        print("Кондиционер включен")

    def turn_off(self):
        print("Кондиционер выключен")

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()

class TVOnCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.turn_on()

    def undo(self):
        self.tv.turn_off()

class TVOffCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.turn_off()

    def undo(self):
        self.tv.turn_on()

class ACOnCommand(Command):
    def __init__(self, ac):
        self.ac = ac

    def execute(self):
        self.ac.turn_on()

    def undo(self):
        self.ac.turn_off()

class ACOffCommand(Command):
    def __init__(self, ac):
        self.ac = ac

    def execute(self):
        self.ac.turn_off()

    def undo(self):
        self.ac.turn_on()

class MacroCommand(Command):
    def __init__(self, commands):
        self.commands = commands

    def execute(self):
        for command in self.commands:
            command.execute()

    def undo(self):
        for command in reversed(self.commands):
            command.undo()

class RemoteControl:
    def __init__(self):
        self.command_history = deque(maxlen=5)

    def press_button(self, command):
        command.execute()
        self.command_history.append(command)

    def press_undo(self):
        if self.command_history:
            command = self.command_history.pop()
            command.undo()
        else:
            print("История пуста, отменять нечего.")

    def show_history(self):
        print("\nИстория команд:")
        for i, cmd in enumerate(self.command_history, 1):
            print(f"{i}. {cmd.__class__.__name__}")

light = Light()
tv = TV()
ac = AC()

remote = RemoteControl()

light_on = LightOnCommand(light)
tv_on = TVOnCommand(tv)
ac_on = ACOnCommand(ac)

light_off = LightOffCommand(light)
tv_off = TVOffCommand(tv)
ac_off = ACOffCommand(ac)

turn_on_all = MacroCommand([light_on, tv_on, ac_on])
turn_off_all = MacroCommand([light_off, tv_off, ac_off])

remote.press_button(light_on)
remote.press_button(tv_on)
remote.press_button(ac_on)

remote.show_history()

remote.press_undo()
remote.show_history()

remote.press_button(turn_on_all)
remote.press_undo()