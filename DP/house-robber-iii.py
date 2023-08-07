# https://leetcode.com/problems/house-robber-iii/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        return max(self.helper(root))
    def helper(self, node):
        if not node:
            return 0, 0
        
        left_with, left_without = self.helper(node.left)
        right_with, right_without = self.helper(node.right)

        max_with = node.val + left_without + right_without
        max_without = max(left_with, left_without) + max(right_with, right_without)

        return max_with, max_without
