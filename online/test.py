"""
interpreter

ON - включить свет
OFF
STATUS - показать текущее состояние

input
"""

from abc import ABC, abstractmethod

#интерфейс команды

class Command(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

#команды
class TurnOnCommand(Command):
    def interpret(self, context):
        context["light"] = "ON"
        print("свет вкл")

class TurnOffCommand(Command):
    def interpret(self, context):
        context["light"] = "OFF"
        print("свет выкл")

class StatucCommand(Command):
    def interpret(self, context):
        print(f"сейчас {context['light']}")

class CommandFactory:
    commands = {
        'ON': TurnOnCommand,
        'OFF': TurnOffCommand,
        'STATUS': StatucCommand
    }

    @staticmethod
    def get_command(command_name):
        return CommandFactory.commands.get(command_name, None)

def main():
    context = {'light': 'OFF'}
    while True:
        command_name = input().strip().upper()
        if command_name == 'EXIT':
            print("выход")
            break

        command_class = CommandFactory.get_command(command_name)
        if command_class:
            command = command_class()
            command.interpret(context)
        else:
            print("неверн ком")

if __name__ == "__main__":
    main()