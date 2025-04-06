from typing import Optional
class Node:
    def __init__(self, val=0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def __init__(self):
        self.visited = {} # keep the dictionary to track any loops. visits.
        '''
        a-b: a is neighbor of b; b is neighbor of a.
        Make a deep copy; RETURN the cloned graph. return cloned starting node.
        '''
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        # if node is in the visited
        if node in self.visited:
            return self.visited[node]
        # node is not in the visited
        # Step 1: make new node
        cloned_node = Node(node.val, [])
        # Step 2: mark the node as visited before getting into the loop
        self.visited[node] = cloned_node
        # Step 3: for each node, visited all the neighbors
        if node.neighbors:
            cloned_node.neighbors =  [self.cloneGraph(n) for n in node.neighbors]

        return cloned_node