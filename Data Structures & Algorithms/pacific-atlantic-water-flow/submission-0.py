class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows, cols = len(heights), len(heights[0])

        pacific_queue = deque()
        atlantic_queue = deque()

        pacific_visited = set()
        atlantic_visited = set()

        for c in range(cols):
            pacific_queue.append((0, c))
            pacific_visited.add((0, c))

            atlantic_queue.append((rows - 1, c))
            atlantic_visited.add((rows - 1, c))

        for r in range(rows):
            pacific_queue.append((r, 0))
            pacific_visited.add((r, 0))

            atlantic_queue.append((r, cols - 1))
            atlantic_visited.add((r, cols - 1))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while pacific_queue:
            r, c = pacific_queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if (nr, nc) not in pacific_visited and heights[nr][nc] >= heights[r][c]:
                        pacific_visited.add((nr, nc))
                        pacific_queue.append((nr, nc))
        result = []
        for r, c in atlantic_visited:
            if (r, c) in pacific_visited:
                result.append([r, c])
        while atlantic_queue:
            r, c = atlantic_queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if (nr, nc) not in atlantic_visited and heights[nr][nc] >= heights[r][c]:
                        atlantic_visited.add((nr, nc))
                        atlantic_queue.append((nr, nc))
                        if (nr, nc) in pacific_visited:
                            result.append([nr, nc])
        return result
