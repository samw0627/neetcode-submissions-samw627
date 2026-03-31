# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def dfs(root,height):
            nonlocal balanced
            if not root:
                return height
            if balanced:
                diff = abs(dfs(root.left,height+1) - dfs(root.right, height+1))
                if diff > 1:
                    balanced = False
            return max(dfs(root.left,height+1),dfs(root.right, height+1))
        
        dfs(root,0)
        return balanced

        