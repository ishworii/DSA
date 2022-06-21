class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


class BinaryTree:
    def __int__(self):
        self.root = None


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end="->")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end="->")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end="->")


if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = Node(6)
    bt.root.left = Node(9)
    bt.root.right = Node(78)
    bt.root.left.left = Node(2)
    bt.root.left.right = Node(5)

    print("Inorder Traversal")
    inorder(bt.root)
    print("---" * 20)

    print("Preorder Traversal")
    preorder(bt.root)
    print("---" * 20)

    print("Poster Traversal")
    postorder(bt.root)
    print("---" * 20)
