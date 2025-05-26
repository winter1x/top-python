"""
command - команда
отправитель команды - клиент
посредник Invoker- официант
Receiver - исполнитель команды - шеф-повар

execute
undo()/redo() - отмена действий, храним историю
"""

"""
создаем команду
передаем команду в invoker
исполнитель выполняет
"""

"""class Light:
    def turn_on(self):
        print("Свет включен")

class Button:
    def __init__(self, light):
        self.light = light

    def press(self):
        self.light.turn_on()


light = Light()
button = Button(light)
button.press()"""
#---------------------------------------------------
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Light:
    def turn_on(self):
        print("Свет включен")

    def turn_off(self):
        print("Свет выключен")

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()

light = Light()
on_command = LightOnCommand(light)
off_command = LightOffCommand(light)

remote = RemoteControl()
remote.set_command(on_command)
remote.press_button()

remote.set_command(off_command)
remote.press_button()

#---------------------------------------------------
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

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

class RemoteControl:
    def __init__(self):
        self.command_history = []

    def set_command(self, command):
        self.command_history.append(command)

    def press_button(self):
        if self.command_history:
            self.command_history[-1].execute()

    def press_undo(self):
        if self.command_history:
            self.command_history.pop().undo()

light = Light()
remote = RemoteControl()

on_command = LightOnCommand(light)
off_command = LightOffCommand(light)

remote.set_command(on_command)
remote.press_button()

remote.press_undo()
