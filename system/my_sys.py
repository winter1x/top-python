import sys
"""
1 можем контролировать аргументы командной строки
    sys.argv - список аргументов

2 завершать выполнение программы
    sys.exit - завершение

3 позволяет общаться с интерпретатором python
    sys.platform - платформа
    win32 - Windows
    linux - Linux
    darwin - MacOS

4 получать информацию о платформе
    sys.version - версия python
    sys.version_info - версия python в виде кортежа

5 управлять путями поиска модулей
    sys.modules - загруженные модули
    sys.path

6 манипулировать вводом и выводом
    sys.stdin ввод
    sys.stdout вывод
    sys.stderr ошибки
    input()
    print()   

7 получать размер объектов в памяти
    sys.getsizeof() - возвращает размер объекта в байтах

8 управлять ограничениями и параметрами интерпретатора
    sys.setrecursionlimit() - устанавливает максимальное количество рекурсивных вызовов

9 флаги запуска интерпретатора
    sys.flags - флаги

10 выходные потоки и перенаправление
    sys.stdout
"""
# 1 python myscript.py input.txt output.txt 
print(sys.argv) # ['myscript.py', 'input.txt', 'output.txt']

"""
input_file = sys.argv[1]
output_file = sys.argv[2]"""

"""if len(sys.argv) < 3:
    print("Please provide input and output files.")
    2 sys.exit(1)"""


"""if not valid_data:
    print('Please provide valid data.')
    sys.exit(1)"""
# 3
print(sys.platform)
if sys.platform.startswith('win'):
    print('windows')

if sys.platform == 'win32':
    print('вы используете windows')

#4
print(sys.version) #3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)
print(sys.version_info) #sys.version_info(major=3, minor=11, micro=5, releaselevel='final', serial=0)

if sys.version_info[1] < 12:
    print('Your version is too low.')
else:
    print('Your version is high.')

#5
import math
print('math' in sys.modules)

print(sys.path)
for path in sys.path:
    print(path)
# sys.path.append('/home/kenny090607/') - для добавления пути к модулю
#6
"""
sys.stdin ввод
sys.stdout вывод
sys.stderr ошибки
input()
print()
"""



"""
text = sys.stdin.readline()
sys.stdout.write(text)
sys.stderr.write('Error')


text = sys.stdin.readline()
sys.stdout.write('вы ввели: ' + text)
sys.stderr.write('Произошла ошибка')
"""
#7
a = [1, 2, 3, 4]
print(sys.getsizeof(a))
#8
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
#9
print(sys.flags.optimize)
#10
"""with open('log.txt', 'w') as log_file:
    sys.stdout = log_file
    print('это печатается в файл')"""

"""
file_filter.py
принимает два аргумента командной строки
    путь к папке, в которой будут искаться файлы
    расширение файлов, которые нужно найти (.txt)

проверка
    что переданы два аргумента
    что путь к папке существует и это папка

проходит по всей вложенной структуре папок (os.walk() или без вложенности)
    ищет файлы с нужным расширением
    выводит список файлов на экран
    общее количества таких файлов и размер

обработка ошибок
    выводим сообщение об ошибке в sys.stderr и завершаем с 1

sys.argv
os.path
os.walk()
os.path.join()
sys.exit
sys.stderr.write
os.path.getsize
os.path.isdir
os.path.exists
"""

#запуск python file_filter.py ./md .md


import os
import sys

def print_error(message):
    sys.stderr.write(f"Ошибка: {message}\n")
    sys.exit(1)

def main():
    if len(sys.argv) < 3:
        print_error("Необходимо передать два аргумента: путь к папке и расширение файлов.")

    directory = sys.argv[1]
    extension = sys.argv[2]

    if not os.path.exists(directory):
        print_error(f"Путь '{directory}' не существует.")
    if not os.path.isdir(directory):
        print_error(f"Путь '{directory}' не является директорией.")

    total_files = 0
    total_size = 0
    matched_files = []

    for root, dirs, files in os.walk(directory):
        for name in files:
            if name.endswith(extension):
                file_path = os.path.join(root, name)
                try:
                    size = os.path.getsize(file_path)
                except OSError:
                    continue

                total_files += 1
                total_size += size

                relative_path = os.path.relpath(file_path, start=directory)
                matched_files.append((relative_path, size))

    print(f'Найдено {total_files} файлов с расширением "{extension}":')

    for path, size in matched_files:
        print(f"- {os.path.join(directory, path)} ({size} байт)")

    print(f"\nОбщий размер: {total_size} байт")

if __name__ == "__main__":
    main()


# утилита сис админа
"""
analyzer.py

принимать путь к папке из аргументов командной строки. sys.argv если аргументов нет - сообщение об ошибке и выход с кодом 1
проверять существование os.path.exists и является ли путь директорией. Если неверный - заверить с 2
выводить список файлов с их размерами. os.listdir os.path.join os.path.getsize os.path.isfile
позволяет дополнительно отфильтровать файлы по расширению (только .txt например) если пользователь передал второй аргумент os.path.splitext
показывает общую информацию о среде выполения os.name os.getcwd os.environ.get sys.version
    ос
    рабочая dir
    PATH
    sys.version

sys.exit

"""

#import os
#import sys

def main():
    if len(sys.argv) < 2:
        print("Необходимо передать путь к папке.")
        sys.exit(1)

    folder_path = sys.argv[1]
    ext_filter = sys.argv[2] if len(sys.argv) > 2 else None

    if not os.path.exists(folder_path):
        print(f"Ошибка: Путь '{folder_path}' не существует.")
        sys.exit(2)

    if not os.path.isdir(folder_path):
        print(f"Ошибка: Путь '{folder_path}' не является директорией.")
        sys.exit(2)

    print(f"\nСодержимое папки '{folder_path}':\n")
    all_entries = os.listdir(folder_path)
    files = []

    for entry in all_entries:
        full_path = os.path.join(folder_path, entry)
        if os.path.isfile(full_path):
            if ext_filter:
                name, ext = os.path.splitext(entry)
                if ext != ext_filter:
                    continue

            size = os.path.getsize(full_path)
            files.append((entry, size))

    if not files:
        print('Файлы не найдены.')
    else:
        for filename, size in files:
            print(f"{filename} - ({size} байт)")

    print("\nОбщая информация о системе:")
    print(f"Операционная система: {os.name}")
    print(f"Текущий рабочий директория: {os.getcwd()}")
    print(f"PATH: {os.environ.get('PATH')}")
    print(f"Python версия: {sys.version}")
    
    sys.exit(0)