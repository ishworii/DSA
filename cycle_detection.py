from linked_list import LinkedList


# set method
def detect_cycle(head):
    s = set()
    while head is not None:
        if head in s:
            return True
        s.add(head)
        head = head.next
    return False


# floyd cycle detection
def floyd_detection(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


if __name__ == "__main__":
    ll = LinkedList().from_list([1, 2, 3, 4, 5])
    ll.head.next.next.next.next.next = ll.head.next.next
    print(detect_cycle(ll.head))
    print(floyd_detection(ll.head))
