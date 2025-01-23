class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_to_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def remove_from_head(self):
        if not self.head:
            return
        self.head = self.head.next

    def remove_by_value(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def insert_after(self, target_data, new_data):
        current = self.head
        while current:
            if current.data == target_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise ValueError(f"Элемент {target_data} не найден в списке")

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def clear(self):
        self.head = None

    def get_at_index(self, index):
        if index < 0:
            raise IndexError("Index cannot be negative")
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            current = current.next
            count += 1
        raise IndexError("Index out of range")

    def remove_at_index(self, index):
        if index < 0:
            raise IndexError("Index cannot be negative")
        if index == 0:
            self.remove_from_head()
            return
        current = self.head
        count = 0
        while current:
            if count == index - 1:
                if current.next:
                    current.next = current.next.next
                else:
                    raise IndexError("Index out of range")
                return
            current = current.next
            count += 1
        raise IndexError("Index out of range")

    def is_empty(self):
        return self.head is None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def merge(self, other):
        if not self.head:
            self.head = other.head
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = other.head


ll = LinkedList()

ll.add_to_tail(10)
ll.add_to_tail(20)
ll.add_to_tail(30)

print("Список после добавления элементов:")
ll.print_list()

ll.add_to_head(5)
print("\nСписок после добавления в начало:")
ll.print_list()

ll.remove_from_head()
print("\nСписок после удаления из начала:")
ll.print_list()

ll.remove_by_value(20)
print("\nСписок после удаления значения 20:")
ll.print_list()

print("\nПоиск элемента 10:")
print(ll.find(10))
print("Поиск элемента 15:")
print(ll.find(15))

print("\nДлина списка:")
print(ll.length())

ll.insert_after(10, 15)
print("\nСписок после вставки 15 после 10:")
ll.print_list()

ll.reverse()
print("\nСписок после реверсирования:")
ll.print_list()

ll.clear()
print("\nСписок после очистки:")
ll.print_list()

ll.add_to_tail(100)
ll.add_to_tail(200)
ll.add_to_tail(300)

print("\nЭлемент с индексом 1:")
print(ll.get_at_index(1))

ll.remove_at_index(1)
print("\nСписок после удаления элемента с индексом 1:")
ll.print_list()

print("\nСписок пуст?")
print(ll.is_empty())

ll2 = LinkedList()
ll2.add_to_tail(400)
ll2.add_to_tail(500)
ll.merge(ll2)
print("\nСписок после объединения:")
ll.print_list()

"""
print_list -> __str__ для строкового представления списка
length -> __len__ для получения длины списка
get_at_index -> __getitem__ для доступа по индексу
find -> __contains__ для проверки наличия элемента
is_empty -> __bool__

убрать лишние методы

добавить
__iter__ для итерации по списку
__add__ для объединения двух списков
__eq__ для сравнения двух списков на равенство
__bool__ для проверки, пуст ли список
"""