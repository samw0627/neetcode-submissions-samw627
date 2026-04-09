class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        dist = defaultdict(lambda: float('inf'))
        start = (0, 0)
        dist[start] = grid[0][0]
        heap = [(grid[0][0], start)]

        while heap:
            cost, (r, c) = heapq.heappop(heap)
            if cost > dist[(r, c)]:
                continue
            if (r, c) == (ROW-1, COL-1):
                return cost
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROW and 0 <= nc < COL:
                    new_cost = max(cost, grid[nr][nc])  # ← key difference
                    if new_cost < dist[(nr, nc)]:
                        dist[(nr, nc)] = new_cost
                        heapq.heappush(heap, (new_cost, (nr, nc)))
'''
[3,2]
[0,1]
'''
                
            


                




        

        
        