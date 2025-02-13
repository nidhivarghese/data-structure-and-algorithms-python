# Graph
# 0 --> 2
# 1 --> 2
# 1 --> 3
# 2 --> 0
# 2 --> 1
# 2 --> 3
# 3 --> 1
# 3 --> 2

# Edge List: 1st element in each array in connected to the 2nd element in the array
edge_list = [[0, 2], [1, 2], [1, 3], [2, 0], [2, 1], [2, 3], [3, 1], [3, 2]]

# Adjacent List - index = node => connected to node in []
adj_graph = [[2], [2, 3], [0, 1, 3], [1, 2]]

# Adjacent Matrix - 0 mean not connected to the index; 1 means connected
adj_matrix = [
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]