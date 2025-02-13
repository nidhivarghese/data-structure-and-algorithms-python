# Stacks - Last in, First Out

class Stacks():
    def __init__(self):
        self.arr = []

    def peek(self):
        return self.arr[-1]

    def push(self, value):
        return self.arr.append(value)

    def pop(self):
        poppedItem = self.arr[-1]
        del self.arr[-1]
        return poppedItem

    def print(self):
        stack = []
        for i in range(len(self.arr)-1, -1, -1):
            stack.append(self.arr[i])

        print(stack)


newStack = Stacks()
newStack.push(12)
newStack.push(24)
print(newStack.peek())

newStack.push(48)
newStack.push(96)
newStack.print()

print(newStack.pop())
newStack.print()

# print(newStack.arr)