"""
DataProcessor

загрузка данных
обработка
сохранение

два подкласса с разными форматами (csv/txt/json...)
"""

from abc import ABC, abstractmethod
import json

class DataProcessor(ABC):
    def process(self):
        data = self.load_data()
        process_data = self.process_data(data)
        self.save_data(process_data)

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def process_data(self, data):
        pass

    @abstractmethod
    def save_data(self, data):
        pass

class CSVProcessor(DataProcessor):
    def load_data(self):
        print("загрузка из CSV")
        return ["apple,10", 'banana,5', 'orange,7']

    def process_data(self, data):
        print("обработка из CSV")
        return [{"name": row.split(",")[0], "count": int(row.split(",")[1])} for row in data]

    def save_data(self, data):
        print("сохранение в json")
        print(json.dumps(data, indent=4, ensure_ascii=False))

class TextProcessor(DataProcessor):
    def load_data(self):
        print("загрузка txt")
        return "hello world"

    def process_data(self, data):
        print('обработка текста')
        return data.upper()

    def save_data(self, data):
        print('сохранение')
        print(data)

csv_processor = CSVProcessor()
csv_processor.process()

print("------------")

text_processor = TextProcessor()
text_processor.process()