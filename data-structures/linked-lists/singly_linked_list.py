class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, ):
        self.head = None
        self.tail = self.head
        self.length = 0


    def append(self, value):
        newNode = Node(value)
        if self.head:
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = self.head

        self.length += 1

    def prepend(self, value):
        newNode = Node(value)
        if self.head:
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = newNode
            self.tail = self.head

        self.length += 1

    def insert(self, index, value):
        if index == 0:
            return self.prepend(value)
        elif index >= self.length:
            return self.append(value)

        currentNode = self.head
        currentIndex = 0

        while currentIndex != index - 1:
            currentNode = currentNode.next
            currentIndex += 1

        newNode = Node(value)
        newNode.next = currentNode.next
        currentNode.next = newNode

        self.length += 1

    def remove(self, index):
        if index == 0:
            newHead = self.head.next
            self.head = newHead
            self.length -= 1
            return None
        elif index > self.length:
            index = self.length - 1

        #     traverse to index and delete node
        currentNode = self.head
        currentIndex = 0

        while currentIndex != index - 1:
            currentNode = currentNode.next
            currentIndex += 1

        if index == self.length -1 :
            currentNode.next = None
            self.tail = currentNode
        else:
            currentNode.next = currentNode.next.next

        self.length -= 1
        return None

    def traverse(self):
        node = self.head

        while node:
            print(node.value,  end= " ---> ")
            node = node.next

        print()

newLinkedList = LinkedList()

newLinkedList.append(0)
newLinkedList.append(10)
newLinkedList.append(20)
newLinkedList.append(30)
newLinkedList.append(40)
newLinkedList.append(50)
newLinkedList.append(60)
newLinkedList.traverse()
print(newLinkedList.head.value, newLinkedList.tail.value, newLinkedList.length)


newLinkedList.insert(9, 100)
newLinkedList.traverse()
print(newLinkedList.head.value, newLinkedList.tail.value, newLinkedList.length)


newLinkedList.remove(9)
newLinkedList.traverse()
print(newLinkedList.head.value, newLinkedList.tail.value, newLinkedList.length)
