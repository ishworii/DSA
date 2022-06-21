class Stack:
    def __init__(self, size):
        self.arr = [None] * size
        self.capacity = size
        self.top = -1

    def size(self):
        return self.top + 1

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() == self.capacity

    def push(self, item):
        if self.is_full():
            print("Stack Overflow!!")
            exit(-1)
        self.top += 1
        # print(f"{item} pushed into the stack")
        self.arr[self.top] = item

    def pop(self):
        if self.is_empty():
            print("Stack Underflow!!")
            exit(-1)
        popped = self.arr[self.top]
        self.top = - 1
        # print(f"Popped {popped} for the stack")
        return popped

    def peek(self):
        if self.is_empty():
            exit(-1)
        return self.arr[self.top]

    # TODO
    def push_list(self, arr):
        rem_space = self.capacity - self.top + 1
        pass


if __name__ == "__main__":
    s = Stack(5)
    print(s.is_empty())
    s.push(5)
    s.pop()
    s.push(7)
    s.push(8)
    s.push(9)
    print(s.peek())
