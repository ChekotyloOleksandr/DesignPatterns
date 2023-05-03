class TreeIterator:
    def __init__(self, value):
        self.stack = [value]

    def __next__(self):
        if not self.stack:
            raise StopIteration
        node = self.stack.pop()
        if node.right is not None:
            self.stack.append(node.right)
        if node.left is not None:
            self.stack.append(node.left)
        return node.value


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __iter__(self):
        return TreeIterator(self)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(8)
    root.right.right.right = TreeNode(9)
    for node in root:
        print(node)
