class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.peek())
    print(stack.size())


    while not stack.is_empty():
        print(stack.pop())