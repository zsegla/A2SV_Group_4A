# https://leetcode.com/problems/recover-binary-search-tree/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.swapped1 = None
        self.swapped2 = None
        self.prev = TreeNode(float('-inf'))
        self.inorder(root)
        self.swapped1.val, self.swapped2.val = self.swapped2.val, self.swapped1.val


    def inorder(self, node):
        if not node:
            return

        self.inorder(node.left)

        if node.val <= self.prev.val:
            if not self.swapped1:
                self.swapped1 = self.prev
            if self.swapped1:
                self.swapped2 = node

        self.prev = node

        self.inorder(node.right)
