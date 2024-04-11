# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # perform DFS on both trees, if DFS are equal, return true
        def dfs(node):
            # empty tree
            if not node:
                return []
            # no further leaf nodes, this node is leaf
            if not node.left and not node.right:
                return [node.val]
            # Concatenate the lists containing leaf node values
            return dfs(node.left) + dfs(node.right)
        
        return dfs(root1) == dfs(root2)