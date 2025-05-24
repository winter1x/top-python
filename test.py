import os

# Константа с корневым путём для обхода
ROOT_PATH = r"C:\Users\Ефимов\Downloads\tail"


def print_directory_contents(path, indent=0):
    """
    Рекурсивно печатает структуру папок и файлов,
    исключая файлы .exe, и выводит полностью содержимое каждого файла.

    :param path: Путь к директории
    :param indent: Уровень вложенности для отступа
    """
    try:
        items = os.listdir(path)
    except PermissionError:
        print(" " * indent + "[Доступ запрещен]")
        return
    except FileNotFoundError:
        print(" " * indent + "[Папка не найдена]")
        return

    for item in sorted(items):
        full_path = os.path.join(path, item)

        if os.path.isdir(full_path):
            print(" " * indent + f"[Папка] {item}")
            print_directory_contents(full_path, indent + 4)
        else:
            if not item.lower().endswith('.exe'):
                print(" " * indent + f"{item}")
                try:
                    with open(full_path, 'r', encoding='utf-8') as file:
                        print(" " * (indent + 4) + "--- Содержимое файла ---")
                        for line in file:
                            print(" " * (indent + 4) + line.rstrip())
                        print(" " * (indent + 4) + "--- Конец содержимого ---")
                except UnicodeDecodeError:
                    print(" " * (
                                indent + 4) + "[Ошибка: файл не является текстовым или содержит неподдерживаемую кодировку]")
                except Exception as e:
                    print(" " * (indent + 4) + f"[Ошибка при чтении файла: {e}]")


if __name__ == "__main__":
    print(f"Содержимое папки '{ROOT_PATH}':")
    print_directory_contents(ROOT_PATH)
