"""
iterator
простое дерево, каждый узел может иметь несколько дочерних элементов
итератор перебирает узлы дерева сверху вниз (в порядке добавления)

узлы дерева TreeNode
итератор TreeIterator

__iter__()
__next__()
StopIteration
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __iter__(self):
        return TreeIterator(self)

class TreeIterator:
    def __init__(self, root):
        self.stack = [root]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration
        current_node = self.stack.pop(0)
        self.stack.extend(current_node.children)
        return current_node.value

root = TreeNode("a")
node_b = TreeNode("b")
node_c = TreeNode("c")
node_d = TreeNode("d")
node_e = TreeNode("e")

root.add_child(node_b)
root.add_child(node_c)
node_b.add_child(node_d)
node_b.add_child(node_e)

for node_value in root:
    print(node_value)