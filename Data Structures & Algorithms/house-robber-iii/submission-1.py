# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        #For each root, we will store the choice when we 
       # (1)Rob the currNode and (2)not rob the current Node
        total = 0
        def dfs(root):
            if not root:
                return [0,0]
            #if root is empty, we will return 0,0
            #Robbing the currentNode. We take notRob from root.left and root.right + root.val
            #Not robbing the currentNode. We take rob from left and right subtree
            nonlocal total
            robLeft, notRobLeft = dfs(root.left)
            robRight, notRobRight = dfs(root.right)
            rob = notRobLeft + notRobRight + root.val
            notRob = max(robLeft, notRobLeft) + max(robRight, notRobRight) #Need to determine the maximum of we take the root or not
            return [rob,notRob]
        return max(dfs(root))
            
            

            







        

        