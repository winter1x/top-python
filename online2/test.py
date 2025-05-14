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
class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate(self):
        return f"{self.title}\n\n{self.content}"

class ReportSaver:
    def save_to_file(self, report, filename):
        with open(filename, "w") as file:
            file.write(report.generate())

class ReportExporter:
    def export_to_json(self, report, filename):
        with open(filename, "w") as file:
            json.dump({
                "title": report.title,
                "content": report.content
            }, file)

    def export_to_xml(self, report, filename):
        with open(filename, "w") as file:
            file.write(f"<report><title>{report.title}</title><content>{report.content}</content></report>")

report = Report("Отчет по продажам", "общий доход: $1000")
saver = ReportSaver()
saver.save_to_file(report, "report.txt")
exporter = ReportExporter()
json_output = exporter.export_to_json(report, "report.json")
print(json_output)

def test_export_to_json():
    report = Report("Отчет по продажам", "общий доход: $1000")
    exporter = ReportExporter()
    json_output = exporter.export_to_json(report, "report.json")
    assert json_output == '{"title": "Отчет по продажам", "content": "общий доход: $1000"}'

    