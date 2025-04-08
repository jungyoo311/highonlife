from typing import List
class Solution:
    def countComponents(self, n:int, edges: List[List[int]]) -> int:
        '''
        Step 1: Build Adjacency List
        Step 2: DFS
        Step 3: Count Connected components

        for second pass, use disjoint-set(UnionFind method)
        '''
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in adj[node]:
                dfs(neighbor)
        cnt = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                cnt += 1
        return cnt
            