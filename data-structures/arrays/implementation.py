class myArray():
    def __init__(self):
        self.length = 0
        self.data = {}

    # Lookup / Access
    def get(self, index):
        return self.data[index]

    # Push
    def push(self, item):
        self.data[self.length] = item
        self.length += 1

    # Pop
    def pop(self):
        lastItem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return lastItem

    # Delete
    def delete(self, index):
        item = self.data[index]
        self.shiftItemsLeft(index)
        self.length -= 1
        return item

    def shiftItemsLeft(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i+1]

        del self.data[self.length - 1]

    # Insert
    def insert(self, item, index):
        self.shiftItemsRight(index)
        self.data[index] = item
        self.length += 1


    def shiftItemsRight(self, index):
        for i in range(self.length, index, -1):
            self.data[i] = self.data[i - 1]


newArray = myArray()
newArray.push('hi')
newArray.push('aloha')
newArray.push('Hola')
newArray.push('Bonjour')
newArray.push('Hallo')
newArray.push('hello')

print(newArray.get(0))
print(newArray.length, newArray.data)

poppedItem = newArray.pop()
print(poppedItem)
print(newArray.length, newArray.data)

newArray.delete(1)
print(newArray.length, newArray.data)


print("Array before inserting 'Namaste' :")
print(newArray.length, newArray.data)
newArray.insert('Namaste', 3)
print(newArray.length, newArray.data)