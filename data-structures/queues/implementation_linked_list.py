class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def enqueue(self, value):
        newNode = Node(value)

        if self.length == 0:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.length += 1
        return newNode

    def dequeue(self):
        if self.length == 0:
            return None
        else:
            poppedItem = self.head.value
            self.head = self.head.next
            self.length -= 1
            return poppedItem

    def front(self):
        return self.head.value

    def print(self):
        currentNode = self.head
        queue = []
        while currentNode:
            queue.append(currentNode.value)
            currentNode = currentNode.next
        print(queue)


newQ = Queue()

newQ.enqueue(0)
newQ.enqueue(10)
newQ.enqueue(20)
newQ.print()

print(newQ.dequeue())
newQ.print()

print(newQ.front())