class Queue():
    def __init__(self):
        self.arr = []

    def enqueue(self, value):
        self.arr.append(value)
        return self.arr

    def dequeue(self):
        dequeuedItem = self.arr[0]
        del self.arr[0]
        return dequeuedItem

    def front(self):
        return self.arr[0]

    def print(self):
        print(self.arr)


newQ = Queue()

newQ.enqueue(0)
newQ.enqueue(10)
newQ.enqueue(20)
newQ.print()

print(newQ.dequeue())
newQ.print()

print(newQ.front())