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


root = TreeNode("A")
node_b = TreeNode("B")
node_c = TreeNode("C")
node_d = TreeNode("D")
node_e = TreeNode("E")

root.add_child(node_b)
root.add_child(node_c)
node_b.add_child(node_d)
node_b.add_child(node_e)

for node_value in root:
    print(node_value)
