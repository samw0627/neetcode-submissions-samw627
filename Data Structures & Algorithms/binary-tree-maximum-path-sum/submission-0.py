# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float("-inf")
        #At each node, take account of the maxsum from previous node
        #if currSum < node.val, we wil restart the current ode
        def dfs(node):
            if not node:
                return 0
            leftTree = max(dfs(node.left),0)
            rightTree = max(dfs(node.right),0)
            #Restart from current Node
            self.maxSum = max(self.maxSum, max(leftTree,rightTree)+node.val,leftTree+rightTree+node.val)
            return node.val + max(leftTree,rightTree,0)
        dfs(root)
        return self.maxSum




        
        