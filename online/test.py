"""
История команд

5 последних действий
несколько устройств (тв кондиционер)
комбинация команд (макрос) [f1, f2, f3]
вкл все
выкл все
"""

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