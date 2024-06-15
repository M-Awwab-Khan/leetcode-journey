from collections import deque

class Solution:
    
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def is_in_bound(r, c):
            return 0 <= r < n and 0 <= c < n

        # Initialize distances and queue
        dist = [[float('inf')] * n for _ in range(n)]
        queue = deque()
        
        # Add all 1s to the queue and set their distance to 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))

        # BFS to calculate minimum distance from each cell to nearest 1
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if is_in_bound(nr, nc) and dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
                

        # Initialize maxDistance and queue for the second BFS
        max_distance = [[0] * n for _ in range(n)]
        queue.append((0, 0))
        max_distance[0][0] = dist[0][0]

        # BFS to calculate maximum safeness factor for each cell
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if is_in_bound(nr, nc):
                    new_distance = min(max_distance[r][c], dist[nr][nc])
                    if new_distance > max_distance[nr][nc]:
                        max_distance[nr][nc] = new_distance
                        queue.append((nr, nc))

        return max_distance[n - 1][n - 1]