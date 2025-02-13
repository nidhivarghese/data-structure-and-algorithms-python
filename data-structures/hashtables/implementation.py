class HashTables():
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)

        return hash


    def set(self, key, value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []

        self.data[address].append([key, value])

        return self.data

    def get(self, key):
        address = self._hash(key)
        currentBucket = self.data[address]
        value = None

        if currentBucket:
            for i in range(len(currentBucket)):
                if currentBucket[i][0] == key:
                    value = currentBucket[i][1]

        return value


    def keys(self):
        keyList = [];

        for i in range(len(self.data)):
            if self.data[i]:
                keyList.append(self.data[i][0][0])

        return keyList


    def values(self):
        valueList = []

        for i in range(len(self.data)):
            if self.data[i]:
                valueList.append(self.data[i][0][1])

        return valueList




newHashTable = HashTables(50)
print(newHashTable.set('grapes', 15))
print(newHashTable.set('apples', 50))
print(newHashTable.set('kiwi', 12))
print(newHashTable.get('grapes'))
print(newHashTable.get('kiwi'))
print(newHashTable.get('apple'))
print(newHashTable.keys())
print(newHashTable.values())