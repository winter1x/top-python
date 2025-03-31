"""
mediator
SmartHub - посредник
Light и Thermostat - отправляют команды через посредника
когда включается свет, температура автоматически понижается
"""

from abc import ABC, abstractmethod

class SmartHub(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass