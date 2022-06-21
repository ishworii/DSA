from binary_tree import Node, inorder


def search_recursive(node, data):
    if node is None:
        return False
    elif node.data > data:
        return search_recursive(node.left, data)
    elif node.data < data:
        return search_recursive(node.right, data)
    else:
        return True


def search_iterative(node, data):
    while node is not None:
        if node.data == data:
            return True
        elif data < node.data:
            node = node.left
        else:
            node = node.right
    return False


def insert_recursive(node, data):
    if node is None:
        return Node(data)
    elif node.data > data:
        node.left = insert_recursive(node.left, data)
    else:
        node.right = insert_recursive(node.right, data)
    return node


def insert_iterative(node, data):
    new_node = Node(data)
    curr = node
    prev = None

    while curr is not None:
        prev = curr
        if data < curr.data:
            curr = curr.left
        else:
            curr = curr.right

    if prev is None:
        prev = new_node
        node = prev
        return node

    elif data < prev.data:
        prev.left = new_node
        return node
    else:
        prev.right = new_node
        return node


def find_min_value(node):
    while node.left is not None:
        node = node.left
    return node


def delete_node(node, data):
    if node is None:
        return node
    if data < node.data:
        node.left = delete_node(node.left, data)
    elif data > node.data:
        node.right = delete_node(node.right, data)
    # node found
    else:
        # node has only one or no child
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp
        # if the node has two children
        # find the inorder successor
        temp = find_min_value(node.right)
        node.data = temp.data
        node.right = delete_node(node.right, temp.data)
    return node


def height(node):
    if node is None:
        return 0
    left_height = height(node.left)
    right_height = height(node.right)
    return max(left_height, right_height) + 1


if __name__ == "__main__":
    root = Node(10)
    root = insert_recursive(root, 15)
    root = insert_recursive(root, 5)
    root = insert_recursive(root, 20)
    root = insert_recursive(root, 4)
    root = insert_recursive(root, 78)
    root = insert_recursive(root, 2)
    # root = insert_iterative(root, 1)
    root = insert_iterative(root, 100)
    inorder(root)
    print(search_recursive(root, 2))
    print(search_iterative(root, 8))
    print(find_min_value(root))
    inorder(root)
    print(" ")
    delete_node(root, 20)
    inorder(root)
    print(height(root))
