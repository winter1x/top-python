"""
time
datetime
random
platform -
re
string
math

functools
"""

#pip install название модуля

from platform import *
"""import platform
import platform as pl
from platform import architecture
from platform import architecture as arch"""

print(architecture())  # архитектура
print(machine())  # тип машины
print(node())  # сетевое имя машины
print(platform())  # строка идентифицирующая базовую платформу
print(processor())  # имя процессора
print(system())  # имя ОС
print(release()) # версия ОС
print(version()) # доп информация об ОС
print(python_version()) # версия питона
print(python_build()) # информация о сборке python
print(python_compiler()) # о компиляторе

