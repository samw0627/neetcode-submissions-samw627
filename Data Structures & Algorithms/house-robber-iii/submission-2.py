# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        #At each node, we decide if we rob or not rob the curent node
        #If we rob the current node, we will only rob the grandchildren node

        def dfs(root):
            if not root:
                return [0,0]
            
            left = dfs(root.left)
            right = dfs(root.right)

            rob = root.val+left[0]+right[0]
            notrob = max(left[0],left[1]) + max(right[0],right[1])

            return[notrob,rob]

        res = dfs(root)

        return max(res[0],res[1])


            

        