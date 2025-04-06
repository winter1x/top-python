'''
memento
редактор заметок с отменой и повтором
undo/redo
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
        self._redo_stack.append(current_state)
        return self._undo_stack.pop()

editor = NoteEditor()
history = HistoryManager()

editor.add_text('привет')
history.backup(editor.save())

editor.show()