# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.i = 0
        def helper(max_val = float("inf")):
            if self.i >= len(preorder) or preorder[self.i] > max_val:
                return None
            root = TreeNode(preorder[self.i])
            self.i += 1
            root.left = helper(root.val)
            root.right = helper(max_val)
            return root

        return helper()
