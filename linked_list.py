class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    @staticmethod
    def from_list(arr):
        ll = LinkedList()
        for each_element in arr[::-1]:
            ll.insert_at_beginning(each_element)
        return ll

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    # will fail in case of duplicate data
    def insert_after(self, after_data, data):
        new_node = Node(data)
        temp = self.head
        while temp.data != after_data:
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def insert_before(self, before_data, data):
        new_node = Node(data)
        if self.head.data == before_data:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            while temp.next.data != before_data:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    def delete(self, node_data):
        if self.head.data == node_data and self.head.next is None:
            self.head = None
        elif self.head.data == node_data and self.head.next is not None:
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next.data != node_data:
                temp = temp.next
            temp.next = temp.next.next

    def reverse_iterative(self):
        prev = None
        curr = self.head
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def reverse_recursive(self, head):
        if head is None or head.next is None:
            return head
        rest = self.reverse_recursive(head.next)

        # first element at last
        head.next.next = head
        head.next = None

        return rest

    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        self.head = slow

    def __repr__(self):
        temp = self.head
        res = []
        while temp is not None:
            res.append(temp.data)
            temp = temp.next
        res = list(map(str, res))
        return "->".join(res)


if __name__ == "__main__":
    l = LinkedList.from_list([1, 2, 3, 4, 5])
    l.insert_at_end(6)
    print(l)
    l.insert_at_end(56)
    l.insert_after(56, 76)
    print(l)
    l.insert_before(1, 34)
    print(l)
    l.insert_before(56, 34)
    print(l)
    l.delete(34)
    print(l)
    l.delete(76)
    print(l)
    l.insert_after(56, 888)
    print(l)
    l.delete(888)
    print(l)
    l.reverse_iterative()
    print(l)
    l.head = l.reverse_recursive(l.head)
    print(l)
    l.find_middle()
    print(l)
