"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n,r,c):
            if n == 1:
                return Node(grid[r][c],True,None,None,None,None)
        
            half = n//2
            top_left = dfs(half, r,c)
            top_right = dfs(half, r, c+half)
            bottom_left = dfs(half, r + half, c)
            bottom_right = dfs(half, r+half, c+half)

            #Check for merge
            if (top_left.val == top_right.val == bottom_left.val == bottom_right.val and top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf):
                return Node( top_left.val ,True,None,None,None,None)
            
            return Node(0, False,top_left,top_right, bottom_left, bottom_right)

        return dfs(len(grid),0,0)
        
        


        




        