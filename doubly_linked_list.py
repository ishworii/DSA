class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        temp = self.head
        res = []
        while temp is not None:
            res.append(temp.data)
            temp = temp.next
        res = list(map(str, res))
        return "<->".join(res)

    @staticmethod
    def from_list(arr):
        dl = DoublyLinkedList()
        for each_element in arr[::-1]:
            dl.insert_at_beginning(each_element)
        return dl

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = None
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        new_node.next = None

    def insert_after(self, next_data, data):
        new_node = Node(data)
        temp = self.head
        while temp.data != next_data:
            temp = temp.next
        # if the next_data is the data of the last node
        if temp.next is None:
            new_node.next = None
            temp.next = new_node
            new_node.prev = temp
        else:
            new_node.next = temp.next
            temp.next.prev = new_node
            new_node.prev = temp
            temp.next = new_node

    def delete(self, node_data):
        temp = self.head
        while temp.next.data != node_data:
            temp = temp.next
        if temp.next.next is None:
            temp.next = None
        else:
            temp.next = temp.next.next
            temp.next.next.prev = temp


if __name__ == "__main__":
    dll = DoublyLinkedList.from_list([1, 2, 4, 5, 6])
    print(dll)
    dll.insert_at_beginning(78)
    print(dll)
    dll.insert_at_end(67)
    print(dll)
    dll.insert_after(67, 89)
    print(dll)
    dll.delete(89)
    print(dll)
