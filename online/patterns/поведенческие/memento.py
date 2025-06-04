"""
memento
originator - создатель - создатель состояния
memento - снимок
caretaker - опекун - хранитель - менеджер состояний

undo/redo

преимущества
инкапсуляция
гибкость 
простота отмены изменений

недостатки 
память
сложность

отличие от других паттернов
command сохраняет инструкцию, а мементо хранит состояние объекта
state переключает состояние объекта
prototype клонирует объект
"""
class Memento:
    def __init__(self, text: str, cursor_position: int):
        self._text = text
        self._cursor_position = cursor_position

    def get_saved_state(self):
        return self._text, self._cursor_position

class TextEditor:
    def __init__(self):
        self._text = ''
        self._cursor = 0

    def write(self, text: str):
        self._text = self._text[:self._cursor] + text + self._text[self._cursor:]
        self._cursor += len(text)
        print(f"текст после ввода {self._text}")

    def move_cursor(self, pos: int):
        self._cursor = max(0, min(pos, len(self._text)))

    def save(self) -> Memento:
        print('создание снимка')
        return Memento(self._text, self._cursor)

    def restore(self, memento: Memento):
        self._text, self._cursor = memento.get_saved_state()
        print(f'восстановление состояния {self._text} курсор {self._cursor}')

class History:
    def __init__(self):
        self._states: list[Memento] = []

    def backup(self, memento: Memento):
        self._states.append(memento)
        print('состояние сохранено в историю')

    def undo(self) -> Memento | None:
        if self._states:
            m = self._states.pop()
            print('отмен последнего действия')
            return m
        print('история пуста')
        return None

    # redo через второй стек, при отмене снимок перемещаетс из стека undo в стек redo и наоборот при повторе

editor = TextEditor()
history = History()
editor.write('hi')
history.backup(editor.save())

editor.write(', hiiii')
history.backup(editor.save())

editor.write('undone')
# нет сохраненных состояний
m = history.undo()
if m:
    editor.restore(m)

m = history.undo()
if m:
    editor.restore(m)

m = history.undo()
if m:
    editor.restore(m)
# нет сохраненных состояний

# безопасность 

class _Memento:
    ...

@property
def _state(self):
    ...


'''
memento
редактор заметок с отменой и повтором
сохранять состояние
с реализацией undo/redo
'''
class Memento:
    def __init__(self, text: str):
        self._text = text

    def get_saved_text(self):
        return self._text

class NoteEditor:
    def __init__(self):
        self._text = ''

    def add_text(self, new_text: str):
        self._text += new_text
        print(f"добавлено {new_text}")

    def save(self) -> Memento:
        return Memento(self._text)

    def show(self):
        print(f"текущая заметка {self._text}")

    def restore(self, memento: Memento):
        self._text = memento.get_saved_text()
        print('состояние восстановлено')

class HistoryManager:
    def __init__(self):
        self._undo_stack: list[Memento] = []
        self._redo_stack: list[Memento] = []

    def backup(self, memento: Memento):
        self._undo_stack.append(memento)
        self._redo_stack.clear()

    def undo(self, current_state: Memento) -> Memento | None:
        if not self._undo_stack:
            print('нечего отменять')
            return None
        self._redo_stack.append(current_state)
        return self._undo_stack.pop()

    def redo(self, current_state: Memento) -> Memento | None:
        if not self._redo_stack:
            print('нечего повторять')
            return None
        self._undo_stack.append(current_state)
        return self._redo_stack.pop()

print('--------------------------------------------')
editor = NoteEditor()
history = HistoryManager()

#состояния
history.backup(editor.save())
editor.add_text('1')

history.backup(editor.save())
editor.add_text('2')

history.backup(editor.save())
editor.add_text('3')


#отмена
memento = history.undo(editor.save())
if memento:
    editor.restore(memento)
editor.show()

memento = history.undo(editor.save())
if memento:
    editor.restore(memento)
editor.show()

#повтор
memento = history.redo(editor.save())
if memento:
    editor.restore(memento)
editor.show()

memento = history.redo(editor.save())
if memento:
    editor.restore(memento)
editor.show()

"""
memento
сохранение состояние персонажа Player в игре

хар-ки
level
health
experience
gold

во время игры
повысить уровень
(получить или) потерять здоровье
получить опыт
получить или потерять деньги

user может сохранять и откратываться

Player - Originator
level
health
experience
gold

level_up()
take_damage(amount)
gain_experience(point)
add_gold(amount)
spend_gold(amount)
save_state() - возвращает объект Memento
restore_state(memento) - восстанавливает состояние из объекта Memento

PlayerMemento - Memento
хранит снимок состояния игрока
не дает изменять состояние игрока

Caretaker
управляет созданием и восстановлением снимков состояния игрока
save(player)
undo(player)
(redo(player))
"""