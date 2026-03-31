# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #Traverse the tree, storing the max num in the path
    def goodNodes(self, root: TreeNode) -> int:
        total = 0
        def dfs(root,maxNum):
            nonlocal total
            if not root:
                return None
            if root.val >= maxNum:
                total += 1
                maxNum = root.val
            left = dfs(root.left,maxNum)
            right = dfs(root.right, maxNum)

        dfs(root, float("-inf"))
        return total



         
        

        
        