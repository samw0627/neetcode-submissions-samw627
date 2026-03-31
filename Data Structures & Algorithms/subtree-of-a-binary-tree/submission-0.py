# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isEqual(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isEqual(p.left,q.left) and isEqual(p.right, q.right)
        
        if not root:
            return False
        if isEqual(root,subRoot):
            return True

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)
        

            
        

        