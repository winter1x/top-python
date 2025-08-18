import os
"""
для работы с операционной системой, файлами и папками
.getcwd() - возвращает текущую директорию
.chdir - переход в другую директорию
.mkdir - создание папки
.makedirs - создание вложенных папок
.rmdir - удаление пустой папки
.removedirs - удаление вложенных пустых папок
os.path.exists - проверка существования файла или папки True/False
.remove - удаление файла
.listdir - список файлов и папок в текущей директории
.endswith - проверка на расширение файла
os.path.join - создание пути к файлу кросплатформенно
os.path.basename - название файла
os.path.dirname - путь
os.path.split - кортеж из двух элементов
os.path.getsize - размер файла
os.path.getmtime - время модификации файла
os.path.isfile - проверка является ли путь файлом
os.path.isfolder - проверка является ли путь директорией
.environ - переменные окружения
.name - название операционной системы
.uname - название операционной системы (только для Unix)
"""
print(os.getcwd())  # C:\Users\Ефимов\pythonProjects\top-python
print(os.environ['TEMP']) # C:\Users\Ефимов\AppData\Local\Temp
print(os.environ['USERPROFILE']) # C:\Users\Ефимов
os.environ['MY_VAR'] = 'SOME_VALUE'
print(os.environ['MY_VAR']) # SOME_VALUE
os.chdir('C:/Users/Ефимов/pythonProjects/') #перемещение в 
print(os.getcwd())
try:
    os.mkdir('new_dir_1') # создание папки
    os.makedirs('new_dir/new_dir_1/new_dir_2') # создание папки с вложенными папками
except FileExistsError:
    print('Такая папка уже существует')
    
os.rmdir('new_dir_1') # удаление папки
os.removedirs('new_dir/new_dir_1/new_dir_2') # удаление папки с вложенными папками (папка должна быть пустой)


print(os.path.exists('new_dir')) # проверка существования файла или папки

# os.remove('pythonProject.rar') # удаление файла

files = os.listdir() # список файлов в текущей директории
print(files)

for file in os.listdir():
    if file.endswith('.txt'):
        print(file)

path = os.path.join('folder', 'file.txt') # создание пути к файлу кросплатформенно
print(path)


print('-' * 20)
print(os.path.basename('/path/to/file.txt')) # название файла
print(os.path.dirname('/path/to/file.txt')) # путь
print(os.path.split('/path/to/file.txt')) # кортеж из двух элементов
print('-' * 20)
print(os.path.isfile('folder/file.txt')) # проверка является ли путь файлом
print(os.path.isfile('temp.txt')) # проверка является ли путь файлом
print(os.path.isdir('folder')) # проверка является ли путь директорией
print('-' * 20)
size = os.path.getsize('temp.txt') # размер файла
print(size)

import time
mod_time = os.path.getmtime('temp.txt') # время модификации файла
print(time.ctime(mod_time)) # преобразуем в читаемую дату

if os.name == 'nt':
    print('Windows')
elif os.name == 'posix':
    print('Mac OS/Linux/Unix')
else:
    print('Other')
    
# print(os.system('dir'))


"""
проходит по папке, ищет файлы с расширением .txt, выводит их размер
(предполагается 4 строчки кода)
"""
folder = '.'

for name in os.listdir(folder):
    path = os.path.join(folder, name)
    if os.path.isfile(path) and name.endswith('.txt'):
        print(f'{path}: {os.path.getsize(path)}')

"""
1. Работа с текущей директорией
Получите текущую рабочую директорию.
Создайте в ней папку backup.
Перейдите в созданную папку.
os.getcwd(), os.mkdir(), os.chdir()

2. Сканирование папки
Вернитесь в исходную директорию.
Получите список всех файлов и папок в директории.
Отфильтруйте только файлы.
os.isfile() os.listdir(), os.path.isfile(), os.path.join()

3. Копирование файлов (эмуляция)
Для каждого файла из пункта 2:
Получите его размер.
Создайте копию с добавлением постфикса _backup в папке backup (только симуляция, без shutil, можно просто создать пустой файл с новым именем).
os.path.getsize(), open(), os.path.basename(), os.path.splitext()

4. Вывод информации о системе
Определите имя операционной системы.
Получите значение переменной окружения HOME или USERPROFILE (в зависимости от ОС).
Выведите PID текущего процесса.
os.name, os.environ.get(), os.getpid()
"""

#import os

def create_backup_folder(path):
    current_dir = os.getcwd()
    backup_path = os.path.join(current_dir, 'backup')
    
    if not os.path.exists(backup_path):
        os.mkdir(backup_path)

    return backup_path

def list_only_files(path):
    all_entries = os.listdir(path)
    files = []
    
    for entry in all_entries:
        full_path = os.path.join(path, entry)
        if os.path.isfile(entry_path):
            files.append(entry)
            
    return files

def simulate_backup(files, dest_folder):
    for file_path in files:
        filename = os.path.basename(file_path)
        name, ext = os.path.splitext(filename)
        backup_name = f'{name}_backup{ext}'
        backup_path = os.path.join(dest_folder, backup_name)

        size = os.path.getsize(file_path)
        print(f'Файл {filename} ({size} байт) будет скопирован в {backup_path}')

        with open(file_path, 'w') as f:
            f.write('')
    

def show_system_info():
    print("\n--- Информация о системе ---")
    print(f"ОС: {os.name}")
    
    home = os.environ.get('HOME') or os.environ.get('USERPROFILE')
    print(f"Домашняя директория: {home}")

    pid = os.getpid()
    print(f"ID текущего процесса: {pid}")


def walk_directory_tree(path, level=0):
    indent = '  ' * level

    for root, dirs, files in os.walk(path):
        print(f"{indent}Папка: {os.path.basename(root)}")

        for file in files:
            file_path = os.path.join(root, file)
            size = os.path.getsize(file_path)
            print(f"{indent}  Файл: {file} ({size} байт)")
        
        break


backup_dir = create_backup_folder()
print(f"Создана папка для бэкапа: {backup_dir}")

current_dir = os.getcwd()
files = list_only_files(current_dir)
print(f"Найдено файлов для бэкапа: {len(files)}")

simulate_backup(files, backup_dir)

show_system_info()

print("\n--- Просмотр дерева директорий ---")
walk_directory_tree(current_dir)