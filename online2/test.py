# Считать с консоли номер дня недели. Вывести буквенную интерпретацию
day = int(input("введите день недели"))
"""if day == 1:
    print('monday')
elif day == 2:
    print('втроник')
elif day == 2:  print('втроник')
elif day==  2:  print('втроник')
elif day == 2:
    print('втроник')
elif day == 2:
    print('втроник')
elif day == 2:
    print('втроник')
    """
match day:
    case 1: print("пн")
    case 2: print("")
    case 3: print("")
    case 4: print("")
    case 5: print("")
    case 6: print("")
    case 7: print("")
    case _: print("нет")