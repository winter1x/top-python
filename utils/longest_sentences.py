#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Нахождение самых длинных предложений в тексте с учётом проблемных мест:
- игнорирование блоков кода (heuristics)
- игнорирование списков (нумерованных "1.", "2." и буллетов "•", "-", "*")
- игнорирование псевдосписков из строк, оканчивающихся на ';'
- корректная нарезка обычных абзацев на предложения

Использование:
  python longest_sentences.py --path text.txt --top 3 --measure words
  python longest_sentences.py --path text.txt --include-lists --include-code

Параметры:
  --path PATH          путь к файлу с текстом (UTF-8)
  --top N              сколько предложений вывести (по умолчанию 3)
  --measure {words,chars}  метрика длины: слова или символы (по умолчанию words)
  --include-lists      включать элементы списков в поиск (по умолчанию выключено)
  --include-code       включать блоки кода в поиск (по умолчанию выключено)
"""

import argparse
import re
from typing import List, Tuple

# --- Регулярки и словари ---------------------------------------------

# 1) Признаки строк кода: ключевые слова/символы, сильная пунктуация, отступы.
_CODE_TOKENS = (
    r'\bdef\b', r'\bclass\b', r'\bimport\b', r'\bfrom\b', r'\breturn\b',
    r'\basync\b', r'\bawait\b', r'#[^\n]*', r'\bfor\b', r'\bwhile\b',
    r'\bif\b', r'\belse\b', r'\belif\b', r'==', r'!=', r'<=', r'>=', r'->',
    r'\(\)', r'\(', r'\)', r':', r'\{', r'\}', r'\[', r'\]', r'=', r'\.',
)

RE_CODE_LINE = re.compile(
    rf'^\s*(?:({"|".join(_CODE_TOKENS)}))|^\s{{4,}}|\t',
    re.IGNORECASE
)

# 2) Маркеры начала пункта списка: буллеты или нумерация "1." / "1)".
RE_LIST_BULLET = re.compile(r'^\s*(?:[•\-\*\u2013\u2014]|[0-9]+\s*[.)])\s+')
# 3) «Список через ;»: подряд ≥2 строк, каждая заканчивается на ';' (или ';' + пробелы)
RE_SEMI_END = re.compile(r';\s*$')

# 4) Разделитель предложений в обычных абзацах: ., !, ?, … (многоточие тоже)
#    Учитываем пробелы/переносы после знака; сохраняем знак в предложение.
RE_SENT_SPLIT = re.compile(r'(?<=[\.!\?…;])\s+')

# 5) Счёт слов: кириллица/латиница/цифры, допускаем дефис внутри слова.
RE_WORD = re.compile(r'[A-Za-zА-Яа-яЁё0-9]+(?:-[A-Za-zА-Яа-яЁё0-9]+)*')


# --- Вспомогательные функции -----------------------------------------

def is_code_line(line: str) -> bool:
    """Грубая эвристика: строка похожа на код?"""
    return bool(RE_CODE_LINE.search(line))


def is_list_line(line: str) -> bool:
    """Строка похожа на пункт списка (буллет или нумерация)?"""
    return bool(RE_LIST_BULLET.match(line))


def looks_like_semicolon_list_block(block_lines: List[str]) -> bool:
    """
    Эвристика «списка через ;»: если в блоке подряд ≥2 непустых
    строк оканчиваются на ';', считаем это списком.
    """
    semicolon_lines = [bool(RE_SEMI_END.search(ln)) for ln in block_lines if ln.strip()]
    return len(semicolon_lines) >= 2 and all(semicolon_lines)


def split_into_blocks(text: str):
    """
    Разбиваем текст на логические блоки: 'para' (обычный абзац), 'list', 'code'.
    Работаем построчно, отслеживаем смену состояния.
    """
    lines = text.replace('\r\n', '\n').replace('\r', '\n').split('\n')

    blocks = []  # список (type, [lines])
    current_type = None
    buf = []

    def flush():
        nonlocal buf, current_type
        if buf:
            blocks.append((current_type or 'para', buf))
            buf = []
            current_type = None

    i = 0
    n = len(lines)
    while i < n:
        ln = lines[i]

        # Пустая строка: завершает текущий блок.
        if not ln.strip():
            flush()
            i += 1
            continue

        # Кандидат на старт блока кода: текущая + хотя бы ещё 1–2 «кодовые» строки.
        if is_code_line(ln):
            j = i + 1
            code_like = 1
            while j < n and (is_code_line(lines[j]) or not lines[j].strip()):
                if is_code_line(lines[j]):
                    code_like += 1
                j += 1
            if code_like >= 2:  # достаточно свидетельств, что это код
                flush()
                blocks.append(('code', lines[i:j]))
                i = j
                continue  # следующий цикл

        # Кандидат на список: буллет/нумерация в ≥2 строках подряд
        if is_list_line(ln):
            j = i + 1
            count = 1
            while j < n and (is_list_line(lines[j]) or not lines[j].strip()):
                if is_list_line(lines[j]):
                    count += 1
                j += 1
            if count >= 2:
                # Возможно, перед первым буллетом есть «префейс» (строки без буллетов)
                # Например: "Например, при:" на отдельной строке.
                # Если предыдущий блок — параграф и последняя его строка НЕ буллет, оставляем его как есть.
                flush()
                blocks.append(('list', lines[i:j]))
                i = j
                continue

        # Проверка «списка через ;» — подряд ≥2 строк оканчиваются на ';'
        # Смотрим мини-блок до следующей пустой строки.
        j = i
        tmp = []
        while j < n and lines[j].strip():
            tmp.append(lines[j])
            j += 1
        if looks_like_semicolon_list_block(tmp):
            flush()
            blocks.append(('list', tmp))
            i = j
            continue

        # Обычный параграф (накапливаем)
        if current_type not in (None, 'para'):
            flush()
        current_type = 'para'
        buf.append(ln)
        i += 1

    flush()
    return blocks


def normalize_para(lines: List[str]) -> str:
    """
    Склеиваем строки абзаца в один текст, аккуратно убирая
    «жёсткие переносы» внутри параграфа.
    """
    # Убираем лишние пробелы и склеиваем через один пробел.
    joined = ' '.join(ln.strip() for ln in lines if ln.strip())
    # Чистим повторяющиеся пробелы
    joined = re.sub(r'\s{2,}', ' ', joined)
    return joined.strip()


def list_items_from_block(lines: List[str]) -> List[str]:
    """
    Преобразуем блок списка в список «предложений»-элементов.
    - Срезаем маркер (буллет/нумерация) в начале строки.
    - Если элемент заканчивается на ';', заменяем на '.' для консистентности.
    """
    items = []
    for ln in lines:
        raw = ln.strip()
        if not raw:
            continue
        # Срезаем маркеры списка
        raw = RE_LIST_BULLET.sub('', raw)
        # Если это список через ';' — нормализуем финал
        raw = raw[:-1] + '.' if raw.endswith(';') else raw
        if raw:
            items.append(raw)
    return items


def sentences_from_para(text: str) -> List[str]:
    """
    Режем обычный абзац на предложения по . ! ? …
    Сохраняем знаки препинания в конце предложения.
    """
    # Простейшая защита от «точек в числах/сокращениях» опускаем — в учебных текстах часто не критично.
    # Если нужно жёстче — можно добавить словарь аббревиатур и предварительную защиту.
    parts = [s.strip() for s in RE_SENT_SPLIT.split(text) if s.strip()]
    return parts


def measure_len(s: str, mode: str) -> int:
    if mode == 'chars':
        return len(s)
    # mode == 'words'
    return len(RE_WORD.findall(s))


def find_longest_sentences(
    text: str,
    top_n: int = 3,
    measure: str = 'words',
    include_lists: bool = False,
    include_code: bool = False,
) -> List[Tuple[str, int]]:
    """
    Главная функция: возвращает top_n самых длинных предложений
    как (предложение, длина).
    """
    blocks = split_into_blocks(text)

    candidates: List[str] = []

    for kind, lines in blocks:
        if kind == 'code' and not include_code:
            continue  # игнорируем код
        if kind == 'list' and not include_lists:
            # список целиком игнорируем
            continue
        if kind == 'list' and include_lists:
            items = list_items_from_block(lines)
            candidates.extend(items)
            continue
        # Обычный абзац
        para = normalize_para(lines)
        candidates.extend(sentences_from_para(para))

    # Чистим пустяки и сор: одиночные маркеры, ломаные куски
    cleaned = []
    for s in candidates:
        # выбрасываем строки, которые подозрительно похожи на код или маркеры
        if is_code_line(s):
            continue
        # выбрасываем «обрезки» короче 2 слов
        if measure_len(s, 'words') < 2:
            continue
        cleaned.append(s)

    scored = [(s, measure_len(s, measure)) for s in cleaned]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:top_n]


# --- CLI --------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Find longest sentences with list/code awareness.")
    ap.add_argument('--path', required=True, help='Путь к текстовому файлу (UTF-8)')
    ap.add_argument('--top', type=int, default=3, help='Сколько предложений вывести (по умолчанию 3)')
    ap.add_argument('--measure', choices=['words', 'chars'], default='words',
                    help='Метрика длины: слова или символы (по умолчанию words)')
    ap.add_argument('--include-lists', action='store_true',
                    help='Включать элементы списков (по умолчанию нет)')
    ap.add_argument('--include-code', action='store_true',
                    help='Включать блоки кода (по умолчанию нет)')
    args = ap.parse_args()

    with open(args.path, 'r', encoding='utf-8') as f:
        text = f.read()

    longest = find_longest_sentences(
        text=text,
        top_n=args.top,
        measure=args.measure,
        include_lists=args.include_lists,
        include_code=args.include_code,
    )

    print("Самые длинные предложения:\n")
    for i, (sent, length) in enumerate(longest, 1):
        unit = 'слов' if args.measure == 'words' else 'символов'
        print(f"{i}. ({length} {unit}): {sent}\n")


if __name__ == '__main__':
    main()
