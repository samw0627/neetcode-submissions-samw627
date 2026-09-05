# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #Keep track of the height of left subtree and right subtree
        #Use a global variable to max diameter
        diameter = 0
        def dfs(root):
            #Base Case: Leaf Node
            nonlocal diameter
            if not root:
                return 0
            left_subtree = dfs(root.left)
            right_subtree = dfs(root.right)

            diameter = max(diameter, left_subtree + right_subtree)
            return max(left_subtree,right_subtree)+1
        
        dfs(root)
        return diameter
            

        