# https://leetcode.com/problems/delete-node-in-a-bst/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key > root.val:  # key in right subtree, keep root and update right subtree
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        else:
            if not (root.left and root.right):  # one or no children
                root = root.left or root.right
            else:  # both children
                next_largest = root.right
                while next_largest.left:
                    next_largest = next_largest.left
                root.val = next_largest.val
                root.right = self.deleteNode(root.right, root.val)

        return root
