class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def push(self, value):
        newNode = Node(value)

        newNode.next = self.head
        self.head = newNode

        if self.length == 0:
            self.tail = self.head

        self.length += 1


        return newNode

    def pop(self):
        if self.length == 0:
            return None
        else:
            poppedItem = self.head.value
            self.head = self.head.next
            self.length -= 1
            return poppedItem

    def peek(self):
        return self.head.value

    def print(self):
        currentNode = self.head
        stack = []
        while currentNode:
            stack.append(currentNode.value)
            currentNode = currentNode.next
        print(stack)


newStack = Stack()
newStack.push(0)
newStack.push(10)
newStack.push(20)
newStack.print()

print(newStack.peek())

print(newStack.pop())
newStack.print()

print(newStack.head.value, newStack.tail.value)