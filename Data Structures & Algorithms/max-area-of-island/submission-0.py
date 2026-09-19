class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        max_Area = 0

        def dfs(r:int, c:int)->int:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_Area = max(max_Area, dfs(r,c))
        return max_Area