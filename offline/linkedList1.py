# 5 -> [1, 2, 3] -> 3 -> 5
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def add_to_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')


li = LinkedList()
li.print_list()
li.add_to_tail(10)
li.add_to_tail(20)
li.add_to_tail(30)

li.print_list()