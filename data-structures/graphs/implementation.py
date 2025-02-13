# Unweighted, undirected graph

class Graph():
    def __init__(self):
        self.no_of_node = 0
        self.adjacent_list = {}


    def addVertex(self, node):
        if node in self.adjacent_list.keys():
            return None
        else:
            self.adjacent_list[node] = []
            self.no_of_node += 1
            return self.adjacent_list

    def addEdges(self, node1, node2):
        # check if node2 exists in node1 list
        if node2 not in self.adjacent_list[node1]:
            self.adjacent_list[node1].append(node2)

        # check if node1 exists in node2 list
        if node1 not in self.adjacent_list[node2]:
            self.adjacent_list[node2].append(node1)

        return self.adjacent_list

    def showConnections(self):
        for node in self.adjacent_list:
            print(node, '--> ', end="")
            for conn in self.adjacent_list[node]:
                print(conn, " ", end=" ")
            print()


myGraph = Graph()
myGraph.addVertex(0)
myGraph.addVertex(1)
myGraph.addVertex(2)
myGraph.addVertex(3)
myGraph.addVertex(4)
myGraph.addVertex(5)
myGraph.addVertex(6)

myGraph.addEdges(0, 1)
myGraph.addEdges(0, 2)
myGraph.addEdges(1, 2)
myGraph.addEdges(1, 3)
myGraph.addEdges(2, 4)
myGraph.addEdges(3, 4)
myGraph.addEdges(4, 5)
myGraph.addEdges(5, 6)

myGraph.showConnections()