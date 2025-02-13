class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        newNode = Node(value)

        if self.length == 0:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length += 1

    def prepend(self, value):
        newNode = Node(value)

        if self.length == 0:
            self.head = newNode
            self.tail = self.head
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

        self.length += 1

    def traverse(self):
        node = self.head

        while node:
            print(node.value,  end= " ---> ")
            node = node.next

        print()

    def reverseTraverse(self):
        node = self.tail

        while node:
            print(node.value, end=' ---> ')
            node = node.prev

        print()

    def insert(self, index, value):
        if index == 0:
            return self.prepend(value)
        elif index >= self.length:
            return self.append(value)

        previousNode = None
        currentNode = self.head
        currentIndex = 0

        while currentIndex != index:
            previousNode = currentNode
            currentNode = currentNode.next
            currentIndex += 1

        newNode = Node(value)
        newNode.next = currentNode
        newNode.prev = previousNode
        previousNode.next = newNode
        currentNode.prev = newNode

        self.length += 1

        return None

    def remove(self, index):
        if index == 0:
            newHead = self.head.next
            self.head = newHead
            self.head.prev = None
            self.length -= 1
            return None
        elif index > self.length:
            index = self.length - 1

        #     traverse to index and delete node
        previousNode = None
        currentNode = self.head
        currentIndex = 0

        while currentIndex != index:
            previousNode = currentNode
            currentNode = currentNode.next
            currentIndex += 1

        if index == self.length -1 :
            previousNode.next = None
            self.tail = previousNode
        else:
            previousNode.next = currentNode.next
            currentNode.next.prev = previousNode

        self.length -= 1
        return None


newLinkedList = DoublyLinkedList()
newLinkedList.append(30)
newLinkedList.append(40)
newLinkedList.append(50)
newLinkedList.append(60)
newLinkedList.traverse()
newLinkedList.reverseTraverse()
print(newLinkedList.head.value, newLinkedList.tail.value, newLinkedList.length)

newLinkedList.prepend(20)
newLinkedList.prepend(10)
newLinkedList.prepend(0)
newLinkedList.traverse()
newLinkedList.reverseTraverse()
print(newLinkedList.head.value, newLinkedList.tail.value, newLinkedList.length)

newLinkedList.insert(2, 345)
newLinkedList.traverse()
newLinkedList.reverseTraverse()
print(newLinkedList.head.value, newLinkedList.tail.value, newLinkedList.length)

newLinkedList.remove(2)
newLinkedList.traverse()
newLinkedList.reverseTraverse()
print(newLinkedList.head.value, newLinkedList.tail.value, newLinkedList.length)