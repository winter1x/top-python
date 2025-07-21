import os

IGNORED_DIRS = {'.git', '.vscode', '__pycache__'}
IGNORED_FILE_EXTENSIONS = {'.user'}

def show_directory_structure(root_path, indent=0):
    """Рекурсивно выводит структуру каталога и содержимое допустимых файлов."""
    try:
        entries = os.listdir(root_path)
    except PermissionError:
        print(" " * indent + f"[Ошибка доступа]: {root_path}")
        return
    except FileNotFoundError:
        print(" " * indent + f"[Папка не найдена]: {root_path}")
        return

    for entry in sorted(entries):
        full_path = os.path.join(root_path, entry)

        # Игнорировать скрытые папки и указанные игнорируемые директории
        if os.path.isdir(full_path):
            if entry.startswith('.') or entry in IGNORED_DIRS:
                continue
            print(" " * indent + f"[Папка] {entry}/")
            show_directory_structure(full_path, indent + 4)

        elif os.path.isfile(full_path):
            # Пропуск скрытых файлов и файлов с игнорируемыми расширениями
            _, ext = os.path.splitext(entry)
            if entry.startswith('.') or ext in IGNORED_FILE_EXTENSIONS:
                continue

            print(" " * indent + f"- {entry}")
            show_file_content(full_path, indent + 4)

def show_file_content(file_path, indent=0):
    """Выводит содержимое файла с отступом."""
    print(" " * indent + f"[Содержимое файла: {os.path.basename(file_path)}]")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                print(" " * indent + line.rstrip())
    except Exception as e:
        print(" " * indent + f"[Ошибка чтения файла: {e}]")

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        start_path = sys.argv[1]
    else:
        start_path = input("Введите путь к папке: ").strip()

    if not os.path.isdir(start_path):
        print(f"Указанный путь не является папкой: {start_path}")
    else:
        print(f"Структура папки: {start_path}\n")
        show_directory_structure(start_path)
