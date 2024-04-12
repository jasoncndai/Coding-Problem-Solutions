# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # track whether left or right on each recursion of DFS, as well as zigzag length
        # We are trying to find longest route, so DFS from top makes most sense
        self.ans = 0
        def dfs(node, isLeft, length):
            if not node:
                return
            self.ans = max(self.ans, length)
            if isLeft:
                # If we want to go left, take left node and set isLeft False
                dfs(node.left, False, length + 1)
                # New zig zag route
                dfs(node.right, True, 1)
            else :
                # If we want to go right, take right node and set isLeft True
                dfs(node.right, True, length + 1)
                # New zig zag route
                dfs(node.left, False, 1)
        # explore left and right subtree of each node in DFS
        dfs(root, True, 0)
        dfs(root, False, 0)
        return self.ans
            