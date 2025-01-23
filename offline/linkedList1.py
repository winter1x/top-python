# 5 -> [1, 2, 3] -> 3 -> 5
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self):
        pass

    def add_to_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return ' -> '.join(result) + ' -> None'

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')
    def remove_from_head(self):
        """
        удаление с головы
        :return:
        """
        pass
    def remove_by_value(self):
        """
        удаление по значению
        :return:
        """
        pass
    def find(self):
        """
        поиск элемента
        :return:
        """
        pass
    def length(self):
        """
        длина списка
        :return:
        """
        pass
    def insert_after(self):
        """
        вставка после элемента
        :return:
        """
        pass
    def reverse(self):
        """
        перевернуть
        :return:
        """
        pass
    def clear(self):
        """
        полная очистка
        :return:
        """
        pass
    def get_at_index(self):
        """
        получить по индексу
        :return:
        """
        pass
    def remove_at_index(self):
        """
        удалить по индексу
        :return:
        """
        pass
    def is_empty(self):
        """
        проверка на пустоту
        :return:
        """
        pass
    def merge(self):
        """
        увеличнение на список
        :return:
        """
        pass

li = LinkedList()
li.print_list()
li.add_to_tail(10)
li.add_to_tail(20)
li.add_to_tail(30)
print(li)
li.print_list()