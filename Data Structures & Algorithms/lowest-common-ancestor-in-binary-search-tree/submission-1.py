# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def search(root):
            if q.val >= root.val >= p.val or p.val >= root.val >= q.val:
                return root
            if root.val > p.val and root.val > q.val:
                return search(root.left)
            if root.val < p.val and root.val < q.val:
                return search(root.right)

        return search(root)
        
        #if val > p and val > q, then LCA will be in the left subtree
        #if val <p and val < q. then LCA will be in the right subtree
        #if p< val < q, then it is the current node 

            

        
        


        