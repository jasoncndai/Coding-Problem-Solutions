# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Do DFS, keep track of max value and counter
        def dfs(node, max_val):
            if not node: return 0
            if node.val >= max_val:
                max_val = node.val
                # we have found a good node (new/equal max) increase by 1
                return 1 + dfs(node.left, max_val) + dfs(node.right, max_val)
            # not good, keep recursing
            return dfs(node.left, max_val) + dfs(node.right, max_val)
        return dfs(root, root.val)
        