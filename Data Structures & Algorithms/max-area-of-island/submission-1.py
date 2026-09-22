class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0    
                    queue = deque([(r,c)])
                    current_area = 1
                    directions = [(1,0),(-1,0),(0,1),(0,-1)]

                    while queue : 
                        curr_r,curr_c = queue.popleft()
                        for dr,dc in directions:
                            nr = dr + curr_r
                            nc = dc + curr_c
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                                queue.append((nr,nc))
                                grid[nr][nc] = 0 
                                current_area += 1
                    max_area = max(max_area, current_area)
        return max_area
