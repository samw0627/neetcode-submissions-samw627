# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        string = []
        def dfs(root):
            nonlocal string
            if not root:
                string.append("N")
                string.append(",")

                return
            string.append(str(root.val))
            string.append(",")
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return "".join(string)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        it = iter(vals)
        def dfs(root):
            if root == "N":
                return None
            newNode = TreeNode(int(root))
            newNode.left = dfs(next(it))
            newNode.right = dfs(next(it))
            return newNode

        return dfs(next(it))




