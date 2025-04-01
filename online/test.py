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

class HomeAutomationHub(SmartHub):
    def __init__(self):
        self.devices = {}

    def register_device(self, device):
        self.devices[device.name] = device

    def notify(self, sender, event):
        if sender == "Light" and event == "ON":
            print("SmartHub: Свет включен. Понижаем температуру.")
            if "Thermostat" in self.devices:
                self.devices["Thermostat"].set_temperature(18)
        elif sender == "Light" and event == "OFF":
            print("SmartHub: Свет выключен. Температура возвращается к норме.")
            if "Thermostat" in self.devices:
                self.devices["Thermostat"].set_temperature(22)


class SmartDevice:
    def __init__(self, name, hub):
        self.name = name
        self.hub = hub
        hub.register_device(self)


class Light(SmartDevice):
    def turn_on(self):
        print("💡 Свет включен.")
        self.hub.notify("Light", "ON")

    def turn_off(self):
        print("💡 Свет выключен.")
        self.hub.notify("Light", "OFF")


class Thermostat(SmartDevice):
    def set_temperature(self, temperature):
        print(f"🌡 Термостат установлен на {temperature}°C")


hub = HomeAutomationHub()

light = Light("Light", hub)
thermostat = Thermostat("Thermostat", hub)

light.turn_on()
light.turn_off()
