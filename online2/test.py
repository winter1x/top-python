import json

class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate(self):
        return f"{self.title}\n\n{self.content}"

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(self.generate())

    def export_to_json(self, filename):
        return json.dumps({
            "title": self.title,
            "content": self.content
        })
"""
вопросы:
сколько ответственностей выполняет этот класс?
какие методы можно отнести к другим сферам ответственности, не связанным напрямую с отчетом?
почему такой подход может быть проблемным в будущем?
что будет, если вам нужно будет сохранить отчет в базу данных или экспортировать его в XML?
как вы можете перераспределить ответственность по другим классам?
"""
# ----------------------------------------------------------------
#solid
#s - srp - принцип единой ответственности