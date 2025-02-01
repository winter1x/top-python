"""
Задание 1
 Дано два текстовых файла. Выяснить, совпадают ли
их строки. Если нет, то вывести несовпадающую строку
из каждого файла.
 Задание 2
 Дантекстовыйфайл.Необходимосоздатьновыйфайл
и записать в него следующую статистику по исходному
файлу:
 ■ Количество символов;
 ■ Количество строк;
 ■ Количество гласных букв;
 ■ Количество согласных букв;
 ■ Количество цифр.
 Задание 3
 Дан текстовый файл. Удалить из него последнюю
строку. Результат записать в другой файл.
 Задание 4
 Дан текстовый файл. Найти длину самой длинной
строки.
 1
Задание 5
 Дан текстовый файл. Посчитать сколько раз в нем
встречается заданное пользователем слово.
 Задание 6
 Дан текстовый файл. Найти изаменить в немзадан
ное слово. Что искать и на что заменять определяется
пользователем
"""
# 1
def compare_files(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        lines1, lines2 = f1.readlines(), f2.readlines()
        for l1, l2 in zip(lines1, lines2):
            if l1.strip() != l2.strip():
                print(l1, l2)
# 2
def file_statistics(file, output_file):
    vowels = 'аеёиоуыюяАЕЁИОУЫЭЮЯaeiouAEIOU'
    consonants = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩbcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
        stats = {
            'Количество символов': len(text) - text.count('\n'),
            'Количество строк': text.count('\n') + 1,
            'Количество гласных букв': sum(1 for ch in text if ch in vowels),
            'Количество согласных букв': sum(1 for ch in text if ch in consonants),
            'Количество цифр': sum(1 for ch in text if ch.isdigit())
        }
    with open(output_file, 'w', encoding='utf-8') as out:
        for key, value in stats.items():
            out.write(f"{key}: {value}\n")
# 3

# 4
def longest_line_lenght(file):
    with open(file, 'r', encoding='utf-8') as f:
        return max(map(len, f.readlines()))
# 5
def count_word_occurrences(file, word):
    with open(file, 'r', encoding='utf-8') as f:
        return sum(line.lower().split().count(word.lower()) for line in f)
# 6
compare_files('1.txt', '2.txt')
print(longest_line_lenght('1.txt'))
print(count_word_occurrences('1.txt', "1"))
file_statistics('1.txt', '3.txt')
