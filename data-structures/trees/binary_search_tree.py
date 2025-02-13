class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree():
    def __init__(self):
        self.root = None


    def insert(self, value):
        newNode = Node(value)

        if self.root is None:
            self.root = newNode
            return newNode
        else:
            current = self.root

            while current is not None:
                if current.value > value:
                    if current.left is not None:
                        current = current.left
                    else:
                        current.left = newNode
                        return newNode
                else:
                    if current.right is not None:
                        current = current.right
                    else:
                        current.right = newNode
                        return newNode

    def delete(self, value):
        current = self.root
        previous = None

        if not(current):
            return None

        while current:
            if value == current.value:
                # No Right Child
                if current.right is None:
                    if previous is None:
                        self.root = current.left
                    else:
                        if current.value < previous.value:
                            previous.left = current.left
                        else:
                            previous.right = current.left

                # No Left Child
                elif current.left is None:
                    if previous is None:
                        self.root = current.right
                    else:
                        if current.value < previous.value:
                            previous.left = current.right
                        else:
                            previous.right = current.right

                # Right Child that has a left child or Left child that has a right child
                elif current.left is None or current.right is None:
                    if previous is None:
                        current = None
                    elif previous.value > current.value:
                        previous.left = None
                    else:
                        previous.right = None

                # Node has both right and left child
                elif current.left is not None and current.right is not None:
                    delete_node = current.right
                    delete_node_parent = current.right

                    while delete_node.left is not None:
                        delete_node_parent = delete_node
                        delete_node = delete_node.left

                    current.value = delete_node.value

                    if delete_node == delete_node_parent:
                        current.right = delete_node.right
                    elif delete_node.right is None:
                        delete_node_parent.left = None
                    else:
                        delete_node_parent.left = delete_node.right
            elif current.value < value:
                # go left
                previous = current
                current = current.left
            else:
                # go right
                previous = current
                current = current.right

        return None


    def find(self, value):
        current = self.root

        if not(current):
            return None

        while current is not None:
            if current.value == value:
                return current
            elif current.value > value:
                current = current.left
            else:
                current = current.right

        return None

    def traverse(self, node):
        tree = { "value": node.value}

        tree["left"] = None if node.left is None else self.traverse(node.left)
        tree["right"] = None if node.right is None else self.traverse(node.right)

        return tree



# Binary Tree:
#           9
#     4           20
# 1       6   15      170


myTree = BinarySearchTree()
myTree.insert(9)
myTree.insert(4)
myTree.insert(6)
myTree.insert(20)
myTree.insert(170)
myTree.insert(15)
myTree.insert(1)

print(myTree.traverse(myTree.root))


node = myTree.find(4)
print(node.value, node.left.value, node.right.value)

myTree.delete(4)
print(myTree.traverse(myTree.root))
