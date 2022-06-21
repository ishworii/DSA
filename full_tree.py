class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_full_tree(root):
    if root is None:
        return True
    elif root.left is None and root.right is None:
        return True
    elif root.left is not None and root.right is not None:
        return is_full_tree(root.left) and is_full_tree(root.right)


if __name__ == "__main__":
    root = Node(56)
    root.right = Node(67)
    root.left = Node(43)
    print(is_full_tree(root))
