# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiam = 0

        def dfs(root):
            nonlocal maxDiam
            #Base Case
            if not root:
                return 0
            #Get the height from the left subTree
            left = dfs(root.left)
            #Get the height from the right subTree
            right = dfs(root.right)
            #Store the maxDiameter
            maxDiam = max(maxDiam, left+right)
            # return the height of the subTree
            return max(left,right)+1
        dfs(root)
        return maxDiam


        