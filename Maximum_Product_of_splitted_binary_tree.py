# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod=10**9+7
        self.max_prod=0
        def totalsum(node):
            if not node:
                return 0
            return node.val+totalsum(node.left)+totalsum(node.right)
        tot=totalsum(root)
        def dfs(node):
            if not node:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            sub=node.val+left+right
            self.max_prod=max(self.max_prod,sub*(tot-sub))
            return sub
        dfs(root)
        return self.max_prod%mod
