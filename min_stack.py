from stack import Stack


class MinStack:
    def __init__(self, size):
        self.s = Stack(size)
        self.aux = Stack(size)

    def push(self, item):
        if self.s.is_full():
            print("Stack Overflow!!!")
            exit(-1)
        self.s.push(item)
        if self.aux.is_empty():
            self.aux.push(item)
        elif item < self.aux.peek():
            self.aux.push(item)

    def pop(self):
        if self.s.is_empty():
            print("Stack Underflow!!!")
            exit(-1)
        popped = self.s.pop()
        if popped == self.aux.peek():
            self.aux.pop()
        return popped

    def min_item(self):
        return self.aux.peek()


if __name__ == "__main__":
    ms = MinStack(5)
    ms.push(10)
    ms.push(4)
    print(ms.min_item())
    print(ms.pop())
    ms.push(2)
    print(ms.min_item())
