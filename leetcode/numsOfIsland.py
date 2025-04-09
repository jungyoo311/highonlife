from typing import List
from collections import deque
class Solution:
    # 1st: DFS approach.
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        For each visit of each grid cell, run dfs recursively for 4 directions.
        filter out out-of-bounds,,,
        '''
        num_islands = 0
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c):
            # filter out edge cases
            if(
                r < 0 or c < 0 or
                r > len(grid) or c > len(grid[0]) or
                grid[r][c] == "0"
            ):
                return False
            # mark as visited
            grid[r][c] = "0"
            # visit all directions
            for rowOffset, colOffset in directions:
                dfs(r + rowOffset, c + colOffset)
            return True
        # 2nd: BFS approach
        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                for rowOffset, colOffset in directions:
                    r, c = row + rowOffset, col + colOffset
                    if(
                        r in range(ROWS) and c in range(COLS) and
                        grid[r][c] == "1" and (r,c) not in visited
                    ):
                        q.append((r,c))
                        visited.add((r,c))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    num_islands += 1
        return num_islands
    
