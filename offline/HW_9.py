def print_triangle_a(n):
    for i in range(n):
        print(" " * i + "*" * (n - i))

def print_triangle_b(n):
    for i in range(n):
        print("*" * (i + 1))

def print_triangle_c(n):
    for i in range(n):
        print(" " * i + "*" * (2 * (n - i) - 1))

def print_triangle_d(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

def print_triangle_e(n):
    for i in range(n - 1, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    for i in range(1, n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

def print_triangle_f(n):
    for i in range(n):
        print("*" * (i + 1) + " " * (2 * (n - i - 1)) + "*" * (i + 1))
    for i in range(n - 2, -1, -1):
        print("*" * (i + 1) + " " * (2 * (n - i - 1)) + "*" * (i + 1))

def print_triangle_g(n):
    for i in range(n):
        print(" " * (n - i - 9) + "*" * (i + 1))
    for i in range(n - 1, -1, -1):
         print(" " * (n - i - 9) + "*" * (i + 1))

def print_triangle_h(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (i + 1))
    for i in range(n - 1, -1, -1):
         print(" " * (n - i - 1) + "*" * (i + 1))

def print_triangle_i(n):
    for i in range(n):
        print("*" * (n - i))

def print_triangle_k(n):
    for i in range(n):
        print(" " * (n - i) + "*" * (i + 1))

def main():
    while True:
        print("\nВыберите фигуру:")
        print("1. Треугольник в верхнем левом углу (а)")
        print("2. Треугольник в нижнем правом углу (б)")
        print("3. Перевернутый треугольник (в)")
        print("4. Равнобедренный треугольник (г)")
        print("5. Заполненный X (д)")
        print("6. Перевернутый заполненный X (е)")
        print("7. Треугольник слева (ж)")
        print("8. Треугольник справа (з)")
        print("9. Треугольник в верхнем левом углу (и)")
        print("10. Треугольник в нижнем правом углу (к)")
        print("11. Выход")

        choice = input("Введите номер: ")

        if choice == '11':
            break

        size = 9

        if choice == '1':
            print_triangle_a(size)
        elif choice == '2':
            print_triangle_b(size)
        elif choice == '3':
            print_triangle_c(size)
        elif choice == '4':
            print_triangle_d(size)
        elif choice == '5':
            print_triangle_e(size)
        elif choice == '6':
            print_triangle_f(size)
        elif choice == '7':
            print_triangle_g(size)
        elif choice == '8':
            print_triangle_h(size)
        elif choice == '9':
            print_triangle_i(size)
        elif choice == '10':
            print_triangle_k(size)
        else:
            print("Неверный ввод.")


if __name__ == "__main__":
    main()
